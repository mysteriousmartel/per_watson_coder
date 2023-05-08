import csv
import json

data = []

student_id = 0
code = 12
comments = 13
statement = 14

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
	with open(path) as file:
		reader = csv.reader(file)
		r_list = [r for r in reader]  # convert csv file to a python list
	return r_list

def parse_file(stop):
	for row in r_list:
		word = "".join(row[code].split()).lower()

		if word == "average" or word == "percenterror" or word == "qualset" or word == "uncertainty":
			append_data(row[statement], word, int(row[student_id]))
		elif word == "dual":
			dual_word = "".join(row[comments].split()).lower()
			words = []

			if "average" in dual_word:
				words.append("average")
			if "percenterror" in dual_word:
				words.append("percenterror")
			if "qualset" in dual_word:
				words.append("qualset")
			if "uncertainty" in dual_word:
				words.append("uncertainty")

			if len(words) == 2:
				data.append({
					"text" : row[statement],
					"labels" : words
					})
		elif word == "other" or word == "none":
			continue
		else:
			print(row[student_id] + " has a bad category")

		if row == stop:
			break

def append_data(content, category, id):
	data.append({
		"text" : content,
		"labels" : [category]
		})

def save_json(file):
	with open(file, 'w', encoding='utf-8') as outfile:
		json.dump(data, outfile, indent=4)

r_list = store_file_data('qsa_even_train_set.csv')
parse_file(113)
save_json('qsa_even_train_set.json')
# save_json(str(len(data)) + '_train_set.json')
data.clear()