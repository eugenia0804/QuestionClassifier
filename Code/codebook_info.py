from Code.utils import get_codebook

def get_codebookinfo(dic,index):
        # Extract the name of the practice at the given index
        practice_name = list(dic.keys())[index-1]
        # Extract the list of subpractices for the given practice name and join them in a single line
        subpractices_list = dic[practice_name]['Subpractices']
        subpractices = "\n`"+"`,\n`".join(subpractices_list)
        explanation = dic[practice_name]['Explanation']
        
        return practice_name, subpractices, explanation

print(get_codebookinfo(get_codebook(),2))