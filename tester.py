import requests
import json
import csv

# Please give IBM time to finish trining the model (~10min) before running, or will return a 422 error

username = "apikey"
password = ""#Insert API key
url = ""#Insert URL
model_id = ""#Insert model_id

statement = 0

stopping_point = #Index of the last row of the .csv
unreachable = 99999

statements = []
label1 = []
label2 = []
machine_code = []

headers = ["Statement", "Label1", "Label2", "Machine Code"]

def create_request(text):
    analyze_request_data = {
        "text": text,
        "language": "en",
        "features": {
            "classifications": {
                "model": model_id
            }
        }
    }

    uri = url + '/v1/analyze'
    params = { 'version': '2021-02-15' }
    headers = {'Content-Type' : 'application/json'}

    ######### Make a call to NLU #########

    response = requests.post(uri,
                             params=params,
                             json=analyze_request_data,
                             headers=headers,
                             auth=(username, password),
                             verify=False,
                            )

    if response.status_code != 200:
        print('Failed to make request to model. Reason:')
        print(response.text)
        label1.append(0)
        label2.append(0)
        machine_code.append("none")
    else:
        print("Successfully analyzed request. Response from NLU:\n")

        response_json = response.json()
        output = json.dumps(response_json, indent=4, sort_keys=True)

        cleaned_output = output.split("\"classifications\": [\n")
        cleaner_output = cleaned_output[1].split("]")

        seperate_output = cleaner_output[0].split("\"class_name\": \"")
        for i in range(1, 5):
            word = seperate_output[i].split("\"")

            if word[0] == "label1":
                score = word[3].split(":")
                cleaned_score = score[1].split("\n")
                float_score = round(float(cleaned_score[0]), 3)
                label1.append(float_score)

            # Use the following commented section for additional labels

            # elif word[0] == "label2":
            #     score = word[3].split(":")
            #     cleaned_score = score[1].split("\n")
            #     float_score = round(float(cleaned_score[0]), 3)
            #     label2.append(float_score)

            else:
                score = word[3].split(":")
                cleaned_score = score[1].split("\n")
                float_score = round(float(cleaned_score[0]), 3)
                label2.append(float_score)

def store_file_data(path): # Opens the CSV Data and Stores the Returns the Data as a List
    with open(path) as file:
        reader = csv.reader(file)
        r_list = [r for r in reader]  # convert csv file to a python list
    return r_list

def parse_file(stop):
    for row in r_list:
        statements.append(row[statement])
        if row == stop:
            break

def save_data(file): # Saving the data to a csv
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for i in range(len(student_ids)):
            writer.writerow([statements[i], label1[i], label2[i], machine_code[i]])

r_list = store_file_data('a.csv') #Change this to the name of the file with the data you would like to analyze
parse_file(stopping_point)
save_data('watson_results.csv')
