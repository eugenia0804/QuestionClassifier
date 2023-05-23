from codebook import get_codebook
from codebookinfo import get_codebookinfo
from question import get_questions
from questioninfo import questions_prompt
import os
import pandas as pd
from langchain.llms import GooglePalm


#model = GooglePalm(model_name = "text-bison-001", google_api_key = os.environ['PALM'])

codebook = get_codebook() # get the codebook dictionary
questions = get_questions()  # get the questions dictionary

def formulate_prompt(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(codebook,practice_index) 
    questioninfo = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    return prompt

def classify_questions(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(codebook,practice_index) 
    questioninfo = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    print(prompt)
    result = model(prompt)  
    return prompt , result


def store_result(index,start_q,end_q): 
  [prompt, results] = classify_questions(index,start_q,end_q)
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
  
#store_result(index = 2, start_q = 20,end_q = 30)
print(formulate_prompt(2, start_q = 20, end_q = 30))