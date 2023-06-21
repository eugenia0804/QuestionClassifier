from code.utils import get_codebook, get_questions
from codebook_info import get_codebookinfo
from question_info import get_questioninfo

def formulate_prompt(index, start_q, end_q):
    codebook = get_codebook()
    practice_name, subpractices = get_codebookinfo(codebook, index)

    INTRO_PROMPT = """
        Inmagine yourself as a education worker, you are developing a series of after-class exercise for high school students.
        You have determined a several practice you want to achieve by designing those question.
        I want you to determine whether the following questions reflect that specific practice or not.\n
        """

    CODEBOOK_PROMPT = f"""
        The name of the practice you need to pay attention to is `{practice_name}`,
        which is consisted of subpractices includes {subpractices}.\n
        """
    
    EXAMPLES = f"""
        User:
        
        
        Assistant:
        {
            {
                "QuestionNumber": "1",
                "Question": "Original text of the question",
                "Reasons": "This question is asking for..., which reflects...",
                "Answer": "Yes/No"
            }
        }
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
            {
                "QuestionNumber": "1",
                "Question": "Original text of the question",
                "Reasons": "This question is asking for..., which reflects...",
                "Answer": "Yes/No"
            }
            {
                "QuestionNumber": "1",
                "Question": "Original text of the question",
                "Reasons": "This question is asking for..., which reflects...",
                "Answer": "Yes/No"
            }
        }
        """


    OUTPUT_PROMPT = f"""
        Return the answer in the a JSON format:\n{OUTPUT_TEMPLATE}
        remember to strickly follow notation rules of json structures
        (eg. required comma & double quotation mark around property names & use single quotation inside of sentences)
        """
        
    SYSTEM_PROMPT = INTRO_PROMPT + CODEBOOK_PROMPT #+ EXAMPLES
    PROMPT = QUESTION_INTRO + QUESTION_TEXT + OUTPUT_PROMPT
    
    return SYSTEM_PROMPT, PROMPT


'''
print('started')
SYSTEM_PROMPT, PROMPT = formulate_prompt(2,10,19)
print(SYSTEM_PROMPT + PROMPT)
'''
