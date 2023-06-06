'''
    Return: Clean df containing question related information
    
    `get_questions()`: This function retrieves the dataset of questions from a given URL and cleans it up by removing any rows with NaN values and reindexing the rows.  
'''

import pandas as pd

# Define a function that retrieves a dataset of questions from a URL
def get_questions():
    questions_url = 'https://raw.githubusercontent.com/eugenia0804/Question-Classifier/main/Dataset/Questionset-TaxonomyMath.csv'
    df_q = pd.read_csv(questions_url)
    # Remove NaN values from the dataset
    df_q = df_q.dropna(subset=['Algorithm Practices'])
    # Reindex the lines of the dataset
    df_q = df_q.reset_index(drop=True)
    df_q.columns = df_q.columns.str.replace('\n', ' ')
    return df_q

get_questions()