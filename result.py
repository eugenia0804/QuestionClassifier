"""
Analyze the result and calculate the percentage of agreement between GPT analysis and human classification.

Returns:
        float: The percentage of result that agrees with the human-entered label.
 """
from main import classify_questions

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

