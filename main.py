from codebook import get_codebook
from codebookinfo import get_codebookinfo
from question import get_questions, questions_prompt
from result import disagreement_calculator

import openai
openai.api_key = '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'
model_engine = "text-davinci-003"

codebook = get_codebook() # get the codebook dictionary
questions = get_questions()  # get the questions dictionary

def classify_questions(practice_index,num_q):
    
    completions = openai.Completion.create(
        codeinfo = get_codebookinfo(codebook,practice_index) 
        questioninfo = questions_prompt(questions, num_q)
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

   
print(classify_questions(0,10))

agreement = disagreement_calculator(questions, codebook, 1, 13)
print(f"{agreement} percent of result agree with each other.")