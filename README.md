# Guide on how to use the Watson trainer and analyzer

(Updated 05/08/2023)

## Background

This series of scripts were developed in the summer of 2021 at the University of Illinois Urbana-Champaign for a project testing IBM's Watson ability to code student responses related to physics questions ([Link to conference paper](https://www.per-central.org/items/perc/5582.pdf)). Our goal was to present a method of semi-automating short-answer data analysis by training a publically available Natural Language Processor (NLP).

To promote further investigation on use of NLPs in grading and data analysis in Physics Education Research, we present our scripts for others to use in their own projects. Please read the instructions carefully when using these scripts.

## Requirements

-Python 3.0 or higher
-An account with [IBM Cloud](https://cloud.ibm.com/registration)
-

The scripts are designed to train and utilize a Watson model to return confidence scores for N number of categories correlated to training data labels. Training data must be converted to a .json format, following the guideline provided by [IBM](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-classifications):

```json
[
  {
    "text": "Example 1",
    "labels": ["label1"]
  },
  {
    "text": "Example 2",
    "labels": ["label1", "label2"]
  }
]
```

Once the training data is prepared, run "trainer.py" to send the training data off for preparing the model. 
