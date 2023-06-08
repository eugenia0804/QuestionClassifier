from code.utils import get_questions

def get_answers(index, start_q, end_q):
    df = get_questions()
    listofkeys = list(df.keys())[3:]
    answer = df[listofkeys[index]][start_q-1:end_q]
    return list(answer)
    
get_answers(3,1,3)



