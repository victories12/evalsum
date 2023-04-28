import pandas as pd
import os
import re
import summa
from summa import summarizer
import csv
from metrics.rouge_l import rouge_l
from metrics.rouge_n import rouge_n
from metrics.bleu import bleu

# read data from the csv file 
Data = pd.read_csv(r'data/wikihowAll/wikihowAll.csv')
Data = Data.astype(str)
rows, columns = Data.shape

# create csv file to store scores
path = "results/wikihowAll"
if not os.path.exists(path): os.makedirs(path)



sum_pre_1 = 0
sum_re_1 = 0
sum_f_1 = 0

sum_pre_2 = 0
sum_re_2 = 0
sum_f_2 = 0

sum_pre_l = 0
sum_re_l = 0
sum_f_l = 0

sum_b = 0
sum_b1 = 0
sum_b2 = 0

for row in range(rows):
    print(f"running row is {row}")
    abstract = Data.iloc[row,Data.columns.get_loc('headline')]      
    article = Data.iloc[row,Data.columns.get_loc('text')]          
    # a threshold is used to remove short articles with long summaries as well as articles with no summary
    if len(abstract) < (0.75*len(article)):
        # remove extra commas 
        abstract = abstract.replace(".,",".")
        #abstract = abstract.encode('utf-8')
        article = re.sub(r'[.]+[\n]+[,]',".\n", article)
        #article = article.encode('utf-8')

        with open('results/wikihowAll/ROUGE_L.csv', 'a') as filel:
            writerl = csv.writer(filel)
            if row == 0:
                writerl.writerow(["number","precision","recall","fscore"])

            # ROUGE_L precision, recall, f_score
            reference = abstract
            candidate = summarizer.summarize(article)
            precision, recall, f_score = rouge_l([candidate], [reference])
            sum_pre_l += precision
            sum_re_l += recall
            sum_f_l += f_score
            writerl.writerow([row, precision, recall, f_score])

        # ROUGE_1
        with open('results/wikihowAll/ROUGE_1.csv', 'a') as file1:
            writer1 = csv.writer(file1)
            if row == 0:
                writer1.writerow(["number","precision","recall","fscore"])
            precision, recall, f_score = rouge_n([candidate], [reference],1)
            writer1.writerow([row, precision, recall, f_score])
            sum_pre_1 += precision
            sum_re_1 += recall
            sum_f_1 += f_score

        # ROUGE_2
        with open('results/wikihowAll/ROUGE_2.csv', 'a') as file2:
            writer2 = csv.writer(file2)
            if row == 0:
                writer2.writerow(["number","precision","recall","fscore"])
            precision, recall, f_score = rouge_n([candidate], [reference],2)
            writer2.writerow([row, precision, recall, f_score])
            sum_pre_2 += precision
            sum_re_2 += recall
            sum_f_2 += f_score

        #BLEU
        with open('results/wikihowAll/BLEU.csv', 'a') as fileb:
            writerb = csv.writer(fileb)
            if row == 0:
                writerb.writerow(["number","bleu","bleu1","bleu2"])
            if len(candidate) ==0 or len(reference) == 0:
                bleu_score = 0
                precisions[0] = 0
                precisions[1] = 0
            else:
                bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference,2)
            writerb.writerow([row, bleu_score, precisions[0], precisions[1]])
            sum_b += bleu_score
            sum_b1 += precisions[0]
            sum_b2 += precisions[1]

print(f"Average scores are:\n  ROUGE_L: Precision {sum_pre_l*1.0/rows} Recall {sum_re_l*1.0/rows} F_score {sum_f_l*1.0/rows}")
print(f"Average scores are:\n  ROUGE_1: Precision {sum_pre_1*1.0/rows} Recall {sum_re_1*1.0/rows} F_score {sum_f_1*1.0/rows}")   
print(f"Average scores are:\n  ROUGE_2: Precision {sum_pre_2*1.0/rows} Recall {sum_re_2*1.0/rows} F_score {sum_f_2*1.0/rows}")
print(f"Average scores are:\n  BLEU: Precision {sum_b*1.0/rows} Recall {sum_b*1.0/rows} F_score {sum_b*1.0/rows}")
print(f"Average scores are:\n  BLEU_1: Precision {sum_b1*1.0/rows} Recall {sum_b1*1.0/rows} F_score {sum_b1*1.0/rows}")
print(f"Average scores are:\n  BLEU_2: Precision {sum_b2*1.0/rows} Recall {sum_b2*1.0/rows} F_score {sum_b2*1.0/rows}")

file1.close()
file2.close()
filel.close()
fileb.close()
    
