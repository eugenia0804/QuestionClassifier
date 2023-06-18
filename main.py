from code.utils import get_codebook, get_questions
from codebook_info import get_codebookinfo
from question_info import questions_prompt
from question_answer import get_answers
from llm import get_llm
import json

iteration = 2
def classify_questions(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(get_codebook(),practice_index) 
    questioninfo = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    llm = get_llm()
    result = llm(prompt)  
    return prompt , result

def store_result(index,start_q,end_q): 
  [prompt, results] = classify_questions(index,start_q,end_q)
  filename = 'results/iteration-2/prompts/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w') as file:
    file.write(prompt)
  filename = 'results/iteration-2/raw_results/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w') as file:
    json.dump(results, file)
    
  final_result = {}
  input_str = results.strip().replace("'", '"')
  '''
  raw_string = re.sub(r'"(.*?)"', r"'\1'", results)
  string = re.sub(r"'(.*?)':", r'"\1":', raw_string)
  input_str = re.sub(r"'(.*?)',", r'"\1",', string)
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
  
  with open('results/iteration-2/results/'+str(start_q)+'to'+str(end_q)+'.json', 'w') as file:
    json.dump(final_result, file)
  return final_result
    
#store_result(index = 2, start_q = 1,end_q = 3)

def run_all(index):
  question_df = get_questions()
  num_questions = question_df.shape[0]
  result_dict = {}
  for i in range(1, num_questions-80, 10):
    result_dict.update(store_result(index, i, i+9))
  keys = result_dict.keys()
  with open('Results/iteration-2/final/1to'+str(num_questions-80)+'.json', 'w') as file:
    json.dump(result_dict, file)
  return 

run_all(2)