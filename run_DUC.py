from os import listdir
from os.path import join
import os
from metrics.rouge_l import rouge_l
from metrics.rouge_n import rouge_n
from metrics.bleu import bleu
import numpy as np
import csv


path_A = "results/DUC2002/A"
path_B = "results/DUC2002/B"
if not os.path.exists(path_A) or not os.path.exists(path_B): 
    os.makedirs(path_A) 
    os.makedirs(path_B)

i = 0

#store the sum of scores of ROUGE_L, ROUGE_1, ROUGE_2, BLEU, BLEU_1, BLEU_2
#data structure like
#[rouge_l precision, rouge_l recall, rouge_l f_score]
#[rouge_1 precision, rouge_1 recall, rouge_1 f_score]
#[rouge_2 precision, rouge_2 recall, rouge_2 f_score]
#[bleu, bleu1, bleu2]

sum_A = np.zeros((4,3))
sum_B = np.zeros((4,3))
for f in listdir("data/DUC2002/referencesA"):
    i += 1
    print(f"Running file No.{i}.")

    with open(join("data/DUC2002/candidates",f[:5] + "_englishSyssum1.txt"), 'r') as file:
        candidate = file.read().replace('\n', '')
    with open(join("data/DUC2002/referencesA",f[:5] + "_englishReference1.txt"), 'r') as file:
        reference_A = file.read().replace('\n', '')
    with open(join("data/DUC2002/referencesB",f[:5] + "_englishReference1.txt"), 'r') as file:
        reference_B = file.read().replace('\n', '')

    # reference A
    # ROUGE_L
    with open('results/DUC2002/A/ROUGE_L.csv', 'a') as file:
        precision, recall, f_score = rouge_l([candidate], [reference_A])
        sum_A[0] = np.add(sum_A[0], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    # ROUGE_1
    with open('results/DUC2002/A/ROUGE_1.csv', 'a') as file:
        precision, recall, f_score = rouge_n([candidate], [reference_A],1)
        sum_A[1] = np.add(sum_A[1], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    # ROUGE_2
    with open('results/DUC2002/A/ROUGE_2.csv', 'a') as file:
        precision, recall, f_score = rouge_n([candidate], [reference_A],2)
        sum_A[2] = np.add(sum_A[2], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    #BLEU
    with open('results/DUC2002/A/BLEU.csv', 'a') as file:
        bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_A,2)
        sum_A[3] = np.add(sum_A[2], np.array([bleu_score,precisions[0], precisions[1]]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","bleu","bleu1","bleu2"])
        writer.writerow([f[:5], bleu_score, precisions[0], precisions[1]])

    # reference B
    # ROUGE_L
    with open('results/DUC2002/B/ROUGE_L.csv', 'a') as file:
        precision, recall, f_score = rouge_l([candidate], [reference_B])
        sum_B[0] = np.add(sum_B[0], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    # ROUGE_1
    with open('results/DUC2002/B/ROUGE_1.csv', 'a') as file:
        precision, recall, f_score = rouge_n([candidate], [reference_B],1)
        sum_B[1] = np.add(sum_B[1], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    # ROUGE_2
    with open('results/DUC2002/B/ROUGE_2.csv', 'a') as file:
        precision, recall, f_score = rouge_n([candidate], [reference_B],2)
        sum_B[2] = np.add(sum_B[2], np.array([precision,recall, f_score]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","precision","recall","fscore"])
        writer.writerow([f[:5],precision, recall, f_score])
    #BLEU
    with open('results/DUC2002/B/BLEU.csv', 'a') as file:
        bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_B,2)
        sum_B[3] = np.add(sum_B[2], np.array([bleu_score,precisions[0], precisions[1]]))
        writer = csv.writer(file)
        if i == 1:
            writer.writerow(["filename","bleu","bleu1","bleu2"])
        writer.writerow([f[:5],bleu_score,precisions[0], precisions[1]])

print(f"For Reference A :")
print(f"Average scores:\nROUGE_L scores: Precision {sum_A[0][0]*1.0/i} Recall {sum_A[0][1]*1.0/i} F_score {sum_A[0][2]*1.0/i}\
      \nROUGE_1 scores: Precision {sum_A[1][0]*1.0/i} Recall {sum_A[1][1]*1.0/i} F_score {sum_A[1][2]*1.0/i}\
      \nROUGE_2 scores: Precision {sum_A[2][0]*1.0/i} Recall {sum_A[2][1]*1.0/i} F_score {sum_A[2][2]*1.0/i}\
      \nBLEU scores: Bleu {sum_A[3][0]*1.0/i} Bleu1 {sum_A[3][1]*1.0/i} Bleu2 {sum_A[3][2]*1.0/i} ")
print(f"For Reference B :")
print(f"Average scores:\nROUGE_L scores: Precision {sum_B[0][0]*1.0/i} Recall {sum_B[0][1]*1.0/i} F_score {sum_B[0][2]*1.0/i}\
      \nROUGE_1 scores: Precision {sum_B[1][0]*1.0/i} Recall {sum_B[1][1]*1.0/i} F_score {sum_B[1][2]*1.0/i}\
      \nROUGE_2 scores: Precision {sum_B[2][0]*1.0/i} Recall {sum_B[2][1]*1.0/i} F_score {sum_B[2][2]*1.0/i}\
      \nBLEU scores: Bleu {sum_B[3][0]*1.0/i} Bleu1 {sum_B[3][1]*1.0/i} Bleu2 {sum_B[3][2]*1.0/i} ")