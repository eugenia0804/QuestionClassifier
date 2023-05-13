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


## Output Structure:

**interation #n:** 
- **prompt.txt**: The prompt used to feed in GPT.
- **raw_first_n.txt**: The immediate output created by GPT in a *list* form.
- **first_n.csv**: Structured results with correspondent correct answers.
