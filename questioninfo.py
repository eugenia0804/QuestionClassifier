"""
    Returns:
            text: Prompt that can be feed to GPT about the question information
            
    `questions_prompt(num_question)`: This function creates a prompt string for a given number of questions by calling the `get_questions()` function to retrieve the dataset, looping through the first `num_question` questions in the dataset, and adding each question's text and a description of the expected output format to the prompt string.

"""
from question import get_questions
import pandas as pd

# Define a function that creates a prompt string for a given number of questions
def questions_prompt(num_question):
    # Call the get_questions function to retrieve a dataset of questions
    df_q = get_questions()
    # Create a prompt string that includes the number of questions to be classified
    prompt = f"Determine whether the following {num_question} questions reflect the given practice or not (Do not try to answer the questions):\n"
    
    # Loop through each question in the dataset
    for i in range (0,num_question):
        question_text = df_q['Question'][i]
         # Create a string that includes the index number and text of the current question
        added_prompt = f"\n{i+1}: {question_text}"
        prompt = prompt + added_prompt
         # Create a string that describes the format of the expected output
    output_example = "\n \nReturn the answer in the following format:\n[Question Number]: [Yes or No?] Explanation:[This question is asking for..., which reflect...]"
     # Add the output example string to the overall prompt string
    prompt = prompt + output_example
    return prompt
