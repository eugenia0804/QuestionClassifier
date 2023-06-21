from Code.utils import get_codebook, get_questions
from codebook_info import get_codebookinfo
from question_info import get_questioninfo

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
        Below is the example input and output: \n
        """
    
    EXAMPLES = """
        User:
        1. Let’s use that test tube model to see how DNA gets made. What patterns do you see after DNA is replicated?
        Does this question reflect the the practice of `Computational Data Practice` or not?
        
        Assistant:
        {
            "1":
                {
                    "Question": "Let’s use that test tube model to see how DNA gets made. What patterns do you see after DNA is replicated?",
                    "Reasons": "To answer this question, student needs to plug in data into the test tube model and formulate thoughts based on observation, which involves the subpractice of `Using computation to analyze data`.",
                    "Answer": "Yes"
                }
        }\n
        """
        
    QUESTION_INTRO = """
        Determine whether the following questions reflect the given practice or not
        (Do not try to answer the questions):\n
        """

    QUESTION_TEXT = f"""
        '''
        {get_questioninfo(start_q, end_q)}
        '''
        """
        
    OUTPUT_TEMPLATE = """
        {
            "Question_number(eg. "1")":
                {
                    "Question": "Original text of question 1",
                    "Reasons": "To answer this question, student needs to ..., which reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
            "Question_number(eg. "2")":
                {
                    "QuestionNumber": "2",
                    "Question": "Original text of question 2",
                    "Reasons": "To answer this question, student needs to ..., which reflect the `practice name`.",
                    "Answer": "Yes/No"
                }
        }
        """


    OUTPUT_PROMPT = f"""
        Return the answer in the a easily dumped JSON format like this \n{OUTPUT_TEMPLATE} （the sample has 2 questions in total)
        remember to strickly follow the rules.
        """
        
    SYSTEM_PROMPT = INTRO_PROMPT + CODEBOOK_PROMPT + EXAMPLES
    PROMPT = QUESTION_INTRO + QUESTION_TEXT + OUTPUT_PROMPT
    
    return SYSTEM_PROMPT, PROMPT

SYSTEM_PROMPT, PROMPT = formulate_prompt(1,1,2)
print("prompt finished")
print(SYSTEM_PROMPT+PROMPT)

