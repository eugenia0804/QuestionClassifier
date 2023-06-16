from code.utils import get_codebook, get_questions
from codebookinfo import get_codebookinfo
from questioninfo import questions_prompt
from questionanswer import get_answers
from llm import get_llm
import json
import pandas as pd 
import seaborn as sns
import matplotlib as plt
from sklearn.metrics import confusion_matrix

def classify_questions(practice_index,start_q,end_q):
    codeinfo = get_codebookinfo(get_codebook(),practice_index) 
    questioninfo = questions_prompt(start_q,end_q)
    prompt = codeinfo + questioninfo
    llm = get_llm()
    result = llm(prompt)  
    return prompt , result

def store_result(index,start_q,end_q): 
  [prompt, results] = classify_questions(index,start_q,end_q)
  filename = 'Results/iteration#2/prompts/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w') as file:
    file.write(prompt)
  filename = 'Results/iteration#2/rawResults/'+str(start_q)+'to'+str(end_q)+'.txt'
  with open(filename, 'w') as file:
    json.dump(results, file)
    
  final_result = {}
  # Populate the DataFrame with data from the results list
  print(results.replace('""',"''"))
  json_res = json.loads(results.replace('""',"''"))
  correct_answers = get_answers(index, start_q, end_q)
  for i, (key, value) in enumerate(json_res.items()):
    correct_answer = "No"
    if correct_answers[i] == 1:
        correct_answer = "Yes"
    value["Correct Answer"] = correct_answer
    final_result[key] = value
  
  with open('Results/iteration#2/results/'+str(start_q)+'to'+str(end_q)+'.json', 'w') as file:
    json.dump(final_result, file)
  return final_result
    
#store_result(index = 2, start_q = 1,end_q = 3)

def run_all(index):
  question_df = get_questions()
  num_questions = question_df.shape[0]
  result_dict = {}
  for i in range(1, num_questions-80, 10):
    result_dict.update(store_result(index, i, i+10))
  keys = result_dict.keys()
  with open('Results/iteration#2/final/1to'+str(num_questions-80)+'.json', 'w') as file:
    json.dump(result_dict, file)
  agreed = 0
  for key in keys:
    answer = result_dict[key]['Answer']
    correct_answer = result_dict[key]['Correct Answer']
  if answer == correct_answer:
    agreed += 1
  agreement_rate = (agreed / len(keys)) * 100
  print("The inner agreement rate between answers and correct answers is {}%".format(agreement_rate))
  
  results = []
  for (question,data) in result_dict.items():
    results.append([data.get("Answer"),data.get("Correct Answer")])
    results_df = pd.DataFrame(results, columns =['Predicted','Actual'])
    conf_mat = confusion_matrix(results_df["Actual"],results_df["Predicted"] )
    sns.heatmap(conf_mat,annot=True,fmt="d")
    plt.savefig("confusion_matrix.png")

run_all(2)
