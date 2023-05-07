'''
    Return: Clean df containing question related information
    
    `get_questions()`: This function retrieves the dataset of questions from a given URL and cleans it up by removing any rows with NaN values and reindexing the rows.  
'''

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