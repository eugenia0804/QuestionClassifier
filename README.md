# CCL-LLM Question Classifier

## Processor Structure:

- **codebook.py** \
Load raw csv file -> Structured Json file storing all the relavent information

- **codebookinfo.py** \
Create the prompt used to teach GPT about the meaning of the category

- **question.py** \
Load raw csv file -> Structured dataframe storiing all the relavent information

- **questioninfo.py** \
Create teh prompt used to feed gpt the information of the questions needed to be categorized.

- **main.py** \
Feed the composite prompt into GPT and get the answers.


## Iterations:
- **iteration#1:** \
    model used: text-davinci-003\
    prompt composition: practice, subpractice, question, instruction\
    results: csv (filtered result), raw_XX.txt (raw result), prompt.txt\
    packages: os, pandas, csv, openai
