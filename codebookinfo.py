"""
    Input: Codebook, index
    Returns:
            text: Prompt that can be feed in GPT about codebook information
    
    This function takes in a codebook dictionary and an index,
    returns a prompt section that explain the practice details as a string.

"""

def get_codebookinfo(dic,index):
        # Extract the name of the practice at the given index
        practice_name = list(dic.keys())[index-1]
        # Extract the list of subpractices for the given practice name and join them in a single line
        subpractices_list = dic[practice_name]['Subpractices']
        subpractices = "\n'"+"',\n'".join(subpractices_list)
        
        # Form up the composite prompt used to feed in GPT.
        prompt = f"The name of the practice is '{practice_name}', which is consisted of subpractices includes {subpractices}.\n \n"
        return prompt
