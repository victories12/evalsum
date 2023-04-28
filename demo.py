
from metrics.rouge_l import rouge_l
from metrics.rouge_n import rouge_n
from metrics.bleu import bleu

#rouge
#precision, recall, f_score
hypothesis = "to make people trustworthy you need to trust them"
reference = "the way to make people trustworthy is to trust them"
print(f"(Precison score, Recall score, F_score)")
print(rouge_l([hypothesis],[reference]))
print(rouge_n([hypothesis],[reference],1))
print(rouge_n([hypothesis],[reference],2))


#bleu
hypothesis = "to make people trustworthy you need to trust them"
reference = "the way to make people trustworthy is to trust them"
bleu, precisions, bp, ratio, candidate_length, reference_length = bleu(hypothesis, reference)
print ("BLEU = ",bleu)
print ("BLEU1 = ",precisions[0])
print ("BLEU2 = ",precisions[1])
print ("BLEU3 = ",precisions[2])
print ("BLEU4 = ",precisions[3])
print ("ratio = ",ratio)
