"""
This file contains a dictionary of coding practices and their subpractices and example questions.
To use this codebook, import this file and call the `get_codebook()` function.
"""

import pandas as pd
import numpy as np

# Load the codebook data file from a URL
code_book_url = 'https://raw.githubusercontent.com/eugenia0804/Question-Classifier/main/Copy%20of%20Bio%20Unit%20Data%20Coding%20-%20Codebook.csv'
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
    codebook[practice] = {'Subpractices':0 ,'Examples': 0}
    subpractices_list = group['Subpractices'].tolist()
    codebook[practice]['Subpractices'] = subpractices_list
    examples_list = []
    examples_list.append(group['Ex1'].tolist()[0])
    examples_list.append(group['Ex2'].tolist()[0])
    examples_list.append(group['Ex3'].tolist()[0])
    codebook[practice]['Examples'] = examples_list

# Define a function to construct the prompt for each practice with its subpractices and examples
def codebook_prompt(dic,index):
    practice_name = list(dic.keys())[index-1]
    subpractices_list = dic[practice_name]['Subpractices']
    subpractices = "\n'"+"',\n'".join(subpractices_list)
    examples_list = dic[practice_name]['Examples']
    examples = "\n'"+"',\n'".join(examples_list)
    prompt = f"The name of the practice is '{practice_name}', which is consisted of subpractices includes {subpractices}.\n \nExample question which reflect this practice includes: {examples}.\n \n"
    return prompt

# Generate a prompt for the first practice
prompt0 = codebook_prompt(codebook,0)
print(prompt0)

# Generate a prompt for the fifth practice
prompt4 = codebook_prompt(codebook,4)
print(prompt4)