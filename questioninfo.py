"""
    Returns:
            text: Prompt that can be feed to GPT about the question information
            
    `questions_prompt(num_question)`: This function creates a prompt string for a given number of questions by calling the `get_questions()` function to retrieve the dataset, looping through the first `num_question` questions in the dataset, and adding each question's text and a description of the expected output format to the prompt string.

"""
from code.utils.question import get_questions
import pandas as pd
import json

template = {
    "Question_number": {
        "Question": "Original text of the question",
        "Reasons": "This question is asking for..., which reflects...",
        "Answer": "Yes/No"
    }
}

# Define a function that creates a prompt string for a given number of questions
def questions_prompt(start_q,end_q):
    # Call the get_questions function to retrieve a dataset of questions
    df_q = get_questions()
    # Create a prompt string that includes the number of questions to be classified
    prompt = f"Determine whether the following {end_q-start_q} questions reflect the given practice or not (Do not try to answer the questions):\n"
    question_num = []
    questions = []
    # Loop through each question in the dataset
    for i in range (start_q-1,end_q):
        question_text = df_q['Question'][i]
        questions.append(question_text)
        question_num.append(i+1)
         # Create a string that includes the index number and text of the current question
        added_prompt = f"\n{i+1}: {question_text}"
        prompt = prompt + added_prompt
         # Create a string that describes the format of the expected output
    output_example = f"\n \nReturn the answer in the a JSON format:\n{template}"
     # Add the output example string to the overall prompt string
    prompt = prompt + output_example
    return prompt

'''
[questioninfo, result_template] = questions_prompt(3)
print(result_template)
'''


