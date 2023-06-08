"""
    Returns:
         json: Codebook which stores the information about the name of the practice, subpractices, and examples
    
    This file contains a dictionary of coding practices and their subpractices and example questions.
    To use this codebook, import this file and call the `get_codebook()` function.

"""

import pandas as pd
import numpy as np

def get_codebook():
    #Load the codebook data file from a URL
    code_book_url = 'https://raw.githubusercontent.com/eugenia0804/Question-Classifier/main/Dataset/BioUnitDataCoding-Codebook.csv'
    df_code = pd.read_csv(code_book_url, skiprows = 2)

    # Rename some of the columns to be more descriptive
    df_code = df_code.rename(columns={'Examples': 'Ex1', 'Unnamed: 4': 'Ex2', 'Unnamed: 5': 'Ex3'})

    # Extract the 'Practices' and 'Explanation' columns into separate variables
    practices = df_code['Practices']
    explanation = df_code['Explanation']

    # Find the indices where the 'Practices' column is not null
    indices = np.where(practices.notnull())[0]
    indices = np.append(indices, len(df_code))

    # Cut the data frame into categories based on the indices of the 'Practices' column
    df_code['practices_index'] = pd.cut(df_code.index, bins=indices-1, labels=False)
    grouped = df_code.groupby(df_code['practices_index'])

    # Create a dictionary with all the information organized by practices
    codebook = {}
    for name, group in grouped:
        practice = group['Practices'].tolist()[0]
        codebook[practice] = {'Explanation':0, 'Subpractices':0 ,'Examples': 0}
        codebook[practice]['Explanation'] = group['Explanation'].tolist()[0]
        subpractices_list = group['Subpractices'].tolist()
        codebook[practice]['Subpractices'] = subpractices_list
        examples_list = []
        examples_list.append(group['Ex1'].tolist()[0])
        examples_list.append(group['Ex2'].tolist()[0])
        examples_list.append(group['Ex3'].tolist()[0])
        codebook[practice]['Examples'] = examples_list
    
    return codebook

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