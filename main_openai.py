from code.utils.codebook import get_codebook
from codebookinfo import get_codebookinfo
from code.utils.question import get_questions
from questioninfo import questions_prompt
from questionanswer import get_answers
import json

import os
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://chatlogo.openai.azure.com"
os.environ["OPENAI_API_KEY"] = os.environ['OPENAI_API_KEY']

from langchain.llms import AzureOpenAI
llm = AzureOpenAI(
    deployment_name="davinci-003",
    max_tokens=3000
)


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
    result = llm(prompt)  
    return prompt , result

def store_result(index,start_q,end_q): 
  [prompt, results] = classify_questions(index,start_q,end_q)
  with open('Results/iteration#2/prompt_1to3.txt', 'w') as file:
    file.write(prompt)
  with open('Results/iteration#2/raw_results_1to3.txt', 'w') as file:
    json.dump(results, file)
    
  final_result = {}
  # Populate the DataFrame with data from the results list
  str_res = results.strip().replace("\n", "").replace("Answer:", "").replace("'",'"')
  json_res = json.loads(str_res)
  correct_answers = get_answers(index, start_q, end_q)
  for i, (key, value) in enumerate(json_res.items()):
    correct_answer = "No"
    if correct_answers[i] == 1:
        correct_answer = "Yes"
    value["Correct Answer"] = correct_answer
    final_result[key] = value
    
  with open('Results/iteration#2/results_1to3.json', 'w') as file:
    json.dump(final_result, file)
  
store_result(index = 2, start_q = 1,end_q = 3)
#print(formulate_prompt(2, start_q = 1, end_q = 3))