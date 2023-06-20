from code.utils import get_questions


# Define a function that creates a prompt string for a given number of questions
def get_questioninfo(start_q,end_q):
    # Call the get_questions function to retrieve a dataset of questions
    df_q = get_questions()
    # Create a prompt string that includes the number of questions to be classified
    question_num = []
    # Loop through each question in the dataset
    questions_txt = ''
    for i in range (start_q-1,end_q):
        question_text = df_q['Question'][i].replace('"','`')
        question_num.append(i+1)
         # Create a string that includes the index number and text of the current question
        added_qtxt = f"\n{i+1}: {question_text}"
        questions_txt = questions_txt + added_qtxt
    return questions_txt

