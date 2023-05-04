from codebook import get_codebook
from codebookinfo import get_codebookinfo
from question import get_questions, questions_prompt

import openai
openai.api_key = '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'
model_engine = "text-davinci-003"

codebook = get_codebook() # get the codebook dictionary
questions = get_questions()  # get the questions dictionary

def classify_questions(practice_index,num_q):
    codeinfo = get_codebookinfo(codebook,practice_index) 
    questioninfo = questions_prompt(num_q)
    completions = openai.Completion.create(
        engine = model_engine,  # specify the GPT-3.5 engine to use
        prompt = codeinfo + '\n \n' + questioninfo,  # concatenate the code and question prompts
        max_tokens=100,  # specify the maximum number of tokens to generate for each completion
        n=1,  
        stop=None,  
        temperature=0,  # specify the sampling temperature for the completion
        )
    answers = completions.choices[0].text.strip().split("\n")  # extract the generated answers from the completion
    
    # return a list of the generated answers in a form of list consisted of 'Yes' or 'No'
    return [a.split(": ")[-1] for a in answers] 



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


print(classify_questions(0,1))

agreement = disagreement_calculator(questions, codebook, 1, 13)
print(f"{agreement} percent of result agree with each other.")
