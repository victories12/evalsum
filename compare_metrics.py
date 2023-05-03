from os import listdir
from os.path import join
import os
from metrics.rouge_l import rouge_l
from metrics.rouge_n import rouge_n
from metrics.bleu import bleu
import numpy as np
import csv
from sacrebleu.metrics import BLEU
bleu_scorer = BLEU()

from rouge import Rouge
rouge_scorer = Rouge()

#Test metrics from library 
sum_A = np.zeros((2,3))
sum_B = np.zeros((2,3))
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
    # ROUGE_L, ROUGE-1, ROUGE-2
    r = rouge_scorer.get_scores(hyps = candidate, refs=reference_A)
    f_1 = [d['rouge-1']['f'] for d in r][0]
    f_2 = [d['rouge-2']['f'] for d in r][0]
    f_l = [d['rouge-l']['f'] for d in r][0]
    sum_A[0] = np.add(sum_A[0], np.array([f_l,f_1, f_2]))
 
    #BLEU

    bleu_score= bleu_scorer.sentence_score(candidate, [reference_A])
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score.score,bleu_score.precisions[0], bleu_score.precisions[1]]))
    
    
    bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_A,4)
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score,precisions[0], precisions[1]]))
    

    # reference B
    # ROUGE_L, ROUGE-1, ROUGE-2
    r = rouge_scorer.get_scores(hyps = candidate, refs=reference_B)
    f_1 = [d['rouge-1']['f'] for d in r][0]
    f_2 = [d['rouge-2']['f'] for d in r][0]
    f_l = [d['rouge-l']['f'] for d in r][0]
    sum_B[0] = np.add(sum_B[0], np.array([f_l,f_1, f_2]))
 
    #BLEU

    bleu_score= bleu_scorer.sentence_score(candidate, [reference_B])
    sum_B[1] = np.add(sum_B[1], np.array([bleu_score.score,bleu_score.precisions[0], bleu_score.precisions[1]]))
    
    
    bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_A,4)
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score,precisions[0], precisions[1]]))
    

print(f"For Reference A :")
print(f"Average scores:\nROUGE_L, ROUGE_1, ROUGE_2 scores:  {sum_A[0][0]*1.0/i}  {sum_A[0][1]*1.0/i}  {sum_A[0][2]*1.0/i}\
\nBLEU scores: Bleu {sum_A[1][0]*1.0/i} Bleu1 {sum_A[1][1]*1.0/i} Bleu2 {sum_A[1][2]*1.0/i} ")

print(f"For Reference B :")
print(f"Average scores:\nROUGE_L, ROUGE_1, ROUGE_2 scores:  {sum_B[0][0]*1.0/i}  {sum_B[0][1]*1.0/i}  {sum_B[0][2]*1.0/i}\
\nBLEU scores: Bleu {sum_B[1][0]*1.0/i} Bleu1 {sum_B[1][1]*1.0/i} Bleu2 {sum_B[1][2]*1.0/i} ")


#Test my metrics

sum_A = np.zeros((2,3))
sum_B = np.zeros((2,3))
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
    # ROUGE_L, ROUGE-1, ROUGE-2
    r = rouge_l([candidate], [reference_A])
    f_l = r[2]
    r = rouge_n([candidate], [reference_A],1)
    f_1 = r[2]
    r = rouge_n([candidate], [reference_A],2)
    f_2 = r[2]
    sum_A[0] = np.add(sum_A[0], np.array([f_l,f_1, f_2]))
 
    #BLEU

    bleu_score, precisions,__, __, __, __= bleu(candidate, reference_A,4)
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score,precisions[0], precisions[1]]))
    
    '''
    bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_A,4)
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score,precisions[0], precisions[1]]))
    '''

    # reference B
    # ROUGE_L, ROUGE-1, ROUGE-2
    r = rouge_l([candidate], [reference_B])
    f_l = r[2]
    r = rouge_n([candidate], [reference_B],1)
    f_1 = r[2]
    r = rouge_n([candidate], [reference_B],2)
    f_2 = r[2]
    sum_B[0] = np.add(sum_B[0], np.array([f_l,f_1, f_2]))
 
    #BLEU

    bleu_score, precisions,__, __, __, __= bleu(candidate, reference_B, 4)
    sum_B[1] = np.add(sum_B[1], np.array([bleu_score,precisions[0], precisions[1]]))    
    '''
    bleu_score, precisions ,__, __, __, __ = bleu(candidate, reference_A,4)
    sum_A[1] = np.add(sum_A[1], np.array([bleu_score,precisions[0], precisions[1]]))
    '''

print(f"For Reference A :")
print(f"Average scores:\nROUGE_L, ROUGE_1, ROUGE_2 scores:  {sum_A[0][0]*1.0/i}  {sum_A[0][1]*1.0/i}  {sum_A[0][2]*1.0/i}\
\nBLEU scores: Bleu {sum_A[1][0]*1.0/i} Bleu1 {sum_A[1][1]*1.0/i} Bleu2 {sum_A[1][2]*1.0/i} ")

print(f"For Reference B :")
print(f"Average scores:\nROUGE_L, ROUGE_1, ROUGE_2 scores:  {sum_B[0][0]*1.0/i}  {sum_B[0][1]*1.0/i}  {sum_B[0][2]*1.0/i}\
\nBLEU scores: Bleu {sum_B[1][0]*1.0/i} Bleu1 {sum_B[1][1]*1.0/i} Bleu2 {sum_B[1][2]*1.0/i} ")

