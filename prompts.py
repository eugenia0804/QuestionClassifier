from Code.utils import get_codebook, get_questions
from Code.codebook_info import get_codebookinfo
from Code.question_info import get_questioninfo

def formulate_prompt(index, start_q, end_q):
    codebook = get_codebook()
    practice_name, subpractices, explanation = get_codebookinfo(codebook, index)

    INTRO_PROMPT = """
        Inmagine yourself as a education worker, you are developing a series of after-class exercise for high school students.
        You have determined a several practice you want to achieve by designing those question.
        I want you to determine whether the following questions reflect that specific practice or not.\n
        """

    CODEBOOK_PROMPT = f"""
        The name of the practice you need to pay attention to is `{practice_name}`,
        which is consisted of subpractices includes {subpractices}.
        The practice is defined as {explanation}.
        Below is one example input and output  (NO NEED TO FOLLOW): \n
        """
    
    if index == 1:
        EXAMPLES = """
        User:
        1. 	Press "Set up" and "Go" to run the simulation. What do you see happening? Does this make sense- remember, there is air resistance?
        Does this question reflect the the practice of `Computational Modeling and Simulation Practices` or not?
        
        Assistant:
        {
            "1":
                {
                    "Question": "Press "Set up" and "Go" to run the simulation. What do you see happening? Does this make sense- remember, there is air resistance?",
                    "Reasons": "To answer this question, student needs to run the simulation and then formulate their thoughts on the model, which involves the subpractice of `Assessing computational models`.",
                    "Answer": "Yes"
                }
        }\n
        """
    if index == 2:
        EXAMPLES = """
        User:
        1.Using the information from this page and the last one, write out the algorithm (the steps) the ribosome must follow to put together the amino acids in the correct order to make a protein based on the mRNA sequence.
        Does this question reflect the the practice of `Algorithm Practice` or not?
        
        Assistant:
        {
            "1":
                {
                    "Question": "Using the information from this page and the last one, write out the algorithm (the steps) the ribosome must follow to put together the amino acids in the correct order to make a protein based on the mRNA sequence.",
                    "Reasons": "To answer this question, student needs to write out the algorithm for a specific context, which involves the subpractice of `Designing and constructing algorithms`.",
                    "Answer": "Yes"
                }
        }\n
        """
    if index == 3:
        EXAMPLES = """
        User:
        1. Let’s use that test tube model to see how DNA gets made. What patterns do you see after DNA is replicated?
        Does this question reflect the the practice of `Computational Data Practice` or not?
        
        Assistant:
        {
            "1":
                {
                    "Question": "Let’s use that test tube model to see how DNA gets made. What patterns do you see after DNA is replicated?",
                    "Reasons": "To answer this question, student needs to plug in data into the test tube model, do the calculation, and then formulate thoughts based on observation, which involves the subpractice of `Using computation to analyze data`.",
                    "Answer": "Yes"
                }
        }\n
        """
    if index == 4:
        EXAMPLES = """
        User:
        1. 	Based on your data, what is the trend of eumelanin levels with respect to hair color?
        Does this question reflect the the practice of `Computational Visualization Practices` or not?
        
        Assistant:
        {
            "1":
                {
                    "Question": "	Based on your data, what is the trend of eumelanin levels with respect to hair color?",
                    "Reasons": "To answer this question, student needs to analyze and visualized the result in order to describe the trend between two variables, which involves the subpractice of `Using a computational visualization to identify and predict trends`.",
                    "Answer": "Yes"
                }
        }\n
        """
        
    QUESTION_INTRO = """
        Determine whether the following questions reflect the given practice or not
        (Do not try to answer the questions):\n
        """

    QUESTION_TEXT = f"""
        '''C
        {get_questioninfo(start_q, end_q)}
        '''
        """
        
    OUTPUT_TEMPLATE1 = """
        {
            "Question_number listed in prompt(eg. "1")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "The question is intended for students to perform the work of ..., which reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
            "Question_number listed in prompt(eg. "2")":
                {
                    "QuestionNumber": "2",
                    "Question": "Original text of question 2",
                    "Reasons": "The focus of the questions is the step to..., which does not reflect any of the listed subpractices.",
                    "Answer": "No"
                }
        }
        """

    OUTPUT_TEMPLATE = """
        {
            "Question_number listed in prompt(eg. "1")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "The question is intended for students to perform the work of ..., which does/does not reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
            ...
             "Question_number listed in prompt(eg. "12")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "The question is intended for students to perform the work of ..., which does/does not reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
        }
        """


    OUTPUT_PROMPT = f"""
        Return the answer in the a easily dumped JSON format like this \n{OUTPUT_TEMPLATE} （the sample has 2 questions in total)
        USe `` if you want to quote some phrases.
        """
        
    SYSTEM_PROMPT = INTRO_PROMPT + CODEBOOK_PROMPT #+ EXAMPLES
    PROMPT = QUESTION_INTRO + QUESTION_TEXT + OUTPUT_PROMPT
    
    return SYSTEM_PROMPT, PROMPT

SYSTEM_PROMPT, PROMPT = formulate_prompt(1,1,2)
print("prompt finished")
print(SYSTEM_PROMPT+PROMPT)

