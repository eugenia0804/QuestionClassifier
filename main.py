from Code.utils import get_questions, get_answers
from prompts import formulate_prompt
from llm import get_llm, get_openai
import json
import pandas as pd
import re

iteration = 2
def classify_questions(index,start_q,end_q):
    sys_prompt, prompt = formulate_prompt(index,start_q,end_q)
    llm = get_openai()
    result = llm(sys_prompt + prompt)  
    print('llm completed')
    return sys_prompt + prompt , result

def store_result(index,start_q,end_q,iteration): 
  [prompt, results] = classify_questions(index,start_q,end_q)
  filename = 'results/iteration-'+str(iteration)+'/prompts/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w', encoding='utf-8') as file:
    file.write(prompt)
  filename = 'results/iteration-'+str(iteration)+'/raw_results/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w', encoding='utf-8') as file:
    json.dump(results, file)
    
  final_result = {}
  input_str = results.strip()#.replace("'", '"')
  '''
  raw_string = re.sub(r'"(.*?)"', r"'\1'", results)
  string = re.sub(r"'(.*?)':", r'"\1":', results)
  i_str = re.sub(r"'(.*?)',", r'"\1",', string)
  input_str = re.sub(r"'(.*?)'}}", r'"\1"}}', i_str)
  '''

  print(input_str)
  json_res = json.loads(input_str)
  correct_answers = get_answers(index, start_q, end_q)
  for i, (key, value) in enumerate(json_res.items()):
    correct_answer = "No"
    if correct_answers[i] == 1:
        correct_answer = "Yes"
    value["Correct Answer"] = correct_answer
    final_result[key] = value
  
  with open('results/iteration-'+str(iteration)+'/results/'+str(start_q)+'to'+str(end_q)+'.json', 'w') as file:
    json.dump(final_result, file)

  if len(final_result) != end_q - start_q:
    print(f"The result from question {start_q} to {end_q} is incomplete.")
    
  return final_result
    
#store_result(index = 2, start_q = 1,end_q = 3)

def run_all(index, iteration):
  question_df = get_questions()
  num_questions = question_df.shape[0]
  result_dict = {}
  for i in range(1, num_questions, 10):
    result_dict.update(store_result(index, i, i+9, iteration))
  keys = result_dict.keys()
  with open('results/iteration-'+str(iteration)+'/final/1to'+str(num_questions-80)+'.json', 'w') as file:
    json.dump(result_dict, file)
  return 

print('work-stream began')
run_all(index = 2, iteration = 2)