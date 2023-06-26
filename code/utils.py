import pandas as pd
import numpy as np
import json
#from questioninfo import questions_prompt
#from codebookinfo import get_codebookinfo

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


# Define a function that retrieves a dataset of questions from a URL
def get_questions():
    questions_url = 'https://raw.githubusercontent.com/eugenia0804/Question-Classifier/main/Dataset/Questionset-TaxonomyMath.csv'
    df_q = pd.read_csv(questions_url)
    # Remove NaN values from the dataset
    df_q = df_q.dropna(subset=['Algorithm Practices'])
    # Reindex the lines of the dataset
    df_q = df_q.reset_index(drop=True)
    df_q.columns = df_q.columns.str.replace('\n', ' ')
    df_q.columns = df_q.columns.str.replace('"','`')
    df_q.columns = df_q.columns.str.replace("'","`")
    return df_q

# define the function to get the human-labeled result in the data file
def get_answers(index, start_q, end_q):
    df = get_questions()
    listofkeys = list(df.keys())[3:]
    answer = df[listofkeys[index]][start_q-1:end_q]
    return list(answer)

'''
def formulate_prompt(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(get_codebook(),practice_index) 
    questioninfo = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    return prompt
'''

#print(json.dumps(get_codebook(),indent = 1))