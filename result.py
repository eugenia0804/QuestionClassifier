import seaborn as sns
import matplotlib as plt
from sklearn.metrics import confusion_matrix

def agreement_cal():
  agreed = 0
  for key in keys:
    answer = result_dict[key]['Answer']
    correct_answer = result_dict[key]['Correct Answer']
  if answer == correct_answer:
    agreed += 1
  agreement_rate = (agreed / len(keys)) * 100
  print("The inner agreement rate between answers and correct answers is {}%".format(agreement_rate))
  
def matrix():
  results = []
  for (question,data) in result_dict.items():
    results.append([data.get("Answer"),data.get("Correct Answer")])
    results_df = pd.DataFrame(results, columns =['Predicted','Actual'])
    conf_mat = confusion_matrix(results_df["Actual"],results_df["Predicted"] )
    sns.heatmap(conf_mat,annot=True,fmt="d")
    plt.savefig("confusion_matrix.png")
