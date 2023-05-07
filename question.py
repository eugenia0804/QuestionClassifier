"""
    Returns:
            text: Prompt that can be feed to GPT about the question information
            
    This file defines two functions for working with a dataset of questions related to mathematics. The functions are:
    1. `get_questions()`: This function retrieves the dataset of questions from a given URL and cleans it up by removing any rows with NaN values and reindexing the rows.  
    2. `questions_prompt(num_question)`: This function creates a prompt string for a given number of questions by calling the `get_questions()` function to retrieve the dataset, looping through the first `num_question` questions in the dataset, and adding each question's text and a description of the expected output format to the prompt string.

"""

import pandas as pd

# Define a function that retrieves a dataset of questions from a URL
def get_questions():
    questions_url = 'https://raw.githubusercontent.com/eugenia0804/Question-Classifier/main/Dataset-Taxonomy-Math.xlsx%20-%20Sheet1.csv'
    df_q = pd.read_csv(questions_url)
    # Remove NaN values from the dataset
    df_q = df_q.dropna(subset=['Question'])
    # Reindex the lines of the dataset
    df_q = df_q.reset_index(drop=True)
    return df_q

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
    output_example = "\n \nReturn the answer in the following format:\n1. Yes or No?:     Explanation:"
     # Add the output example string to the overall prompt string
    prompt = prompt + output_example
    return prompt
