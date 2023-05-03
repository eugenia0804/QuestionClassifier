# CCL-LLM Question Classifier

codebook.py: \
Load raw csv file -> Structured Json file storing all the relavent information

codebookinfo.py: \
Create the prompt used to teach GPT about the meaning of the category

question.py: \
Load raw csv file and forming up prompt providing GPT the questions needed to be categorized.

main.py: \
Feed the composite prompt into GPT and get the answers.


