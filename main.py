from codebook import get_codebook
from codebookinfo import get_codebookinfo
from question import get_questions
from questioninfo import questions_prompt
import os
import json
from langchain.llms import GooglePalm


model = GooglePalm(model_name = "text-bison-001", google_api_key = os.environ['PALM'])

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
  with open('Results/iteration#2/prompt_20to30.txt', 'w') as file:
    file.write(prompt)
  with open('Results/iteration#2/raw_results_20to30.json', 'w') as file:
    json.dump(results, file)
    
  final_result = {}
  # Populate the DataFrame with data from the results list
  for i, result in enumerate(results):
    
      '''
      Insert correct answer into the output dictionary and stored it in final_result
      '''
      
  with open('Results/iteration#2/results_20to30.json', 'w') as file:
    json.dump(final_result, file)
  
#store_result(index = 2, start_q = 20,end_q = 30)
print(formulate_prompt(2, start_q = 20, end_q = 30))