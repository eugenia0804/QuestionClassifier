from codebook import get_codebook
from codebookinfo import get_codebookinfo
from question import get_questions
from questioninfo import questions_prompt
import os
import pandas as pd

import openai

key = os.environ['OpenAI']
openai.api_key = key
model_engine = "text-davinci-003"

codebook = get_codebook() # get the codebook dictionary
questions = get_questions()  # get the questions dictionary

def classify_questions(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(codebook,practice_index) 
    [questioninfo, result_template] = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    completions = openai.Completion.create(
        engine = model_engine,  # specify the GPT-3.5 engine to use
        prompt = codeinfo + questioninfo,  # concatenate the code and question prompts
        max_tokens=(end_q-start_q)*50,  # specify the maximum number of tokens to generate for each completion
        n=1,  
        stop=None,  
        temperature=0.1,  # specify the sampling temperature for the completion
        )
    result = completions.choices[0].text.strip().split("\n")  # extract the X^TXgenerated answers from the completion
    # return a list of the generated answers in a form of list consisted of 'Yes' or 'No'
    return prompt , result, result_template


def store_result(index,start_q,end_q): 

  [prompt, results, result_template] = classify_questions(index,start_q,end_q)
  result_df = result_template
  
  with open('Results/iteration#1/prompt_20to30.txt', 'w') as file:
    file.write(prompt)
  with open('Results/iteration#1/raw_results_20to30.txt', 'w') as file:
    file.write(str(results))



  # Populate the DataFrame with data from the results list
  for i, result in enumerate(results):
      question_number, result_explanation = result.split(': ', 1)
      result_str, explanation = result_explanation.split('. Explanation: ')
      print(codebook.keys())
      practice_name = list(codebook.keys())[index]
      correct_ans = questions[practice_name][i]
      result_df.loc[i, 'Result'] = result_str
      result_df.loc[i, 'Explanation'] = explanation
      result_df.loc[i, 'Correct Answer'] = correct_ans
      
  result_df.to_csv('Results/iteration#1/20to30.csv', index=False)
  
store_result(index = 2, start_q = 20,end_q = 30)
  


'''
def disagreement_calculator(df_q, codebook,practice_index,num_q): 
  # Get the name of the practice from the codebook using the practice_index
  practice_name = list(codebook.keys())[practice_index]
  results = classify_questions(practice_index,num_q)
  # processed_results = [0 if item == 'No'else 1 for item in results]
  
  # Process the results to assign a numerical value to each answer (Yes = 1, No = 0, Not sure = 0.5)
  processed_results = [1 if item == 'Yes' else 0 if item == 'No' else 0.5 for item in results]
  compared_results = df_q[practice_name][0:num_q]
  
  # Count the number of disagreements between the processed and actual answers
  count = 0
  for i in range(0,num_q):
    if processed_results[i] != compared_results[i]:
      count += 1
  # Calculate the fraction of disagreements and return the agreement score (1 - fraction)
  fraction = count/num_q
  return 1-fraction
'''

# agreement = disagreement_calculator(questions, codebook, 1, 13)
# print(f"{agreement} percent of result agree with each other.")