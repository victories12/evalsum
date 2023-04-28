
import collections
import math
import os
import argparse

def load_lines(f_path):
    lines = []
    with open(f_path, "r") as f:
        for line in f:
            line = line.strip('\n').strip('\r')
            fs = line.split()
            lines.append(fs)
    return lines

def transfer_corpus(str_corpus):
    str_corpus = str_corpus.strip('\n').strip('\r')
    str_corpus = str_corpus.split()
    return str_corpus

def count_ngrams(words, n):
    n_grams_list = []
    for i in range(len_ngram(words, n)):
        n_gram = words[i:i+n]
        n_grams_list.append(n_gram)
    return n_grams_list

def len_ngram(words, n):
    return max(len(words) - n + 1, 0)

def count_overlap(candidate_ngrams, reference_ngrams):
    result = 0
    for w in candidate_ngrams:
        for v in reference_ngrams:
            if w == v:
                result += 1
                break
    return result

def bleu(candidate, reference, max_order=4):

    reference_corpus = transfer_corpus(reference)
    candidate_corpus = transfer_corpus(candidate)

    reference_length = len(reference_corpus)
    candidate_length = len(candidate_corpus)

    precisions = [0] * max_order
    for i in range(1, max_order + 1):

        ref_ngram_counts = count_ngrams(reference_corpus, i)
        candidate_ngram_counts =  count_ngrams(candidate_corpus, i)
        matches = count_overlap(ref_ngram_counts, candidate_ngram_counts)

 
        precisions[i-1] = (float(matches) / candidate_length)

    if min(precisions) > 0:
        p_log_sum = sum((1. / max_order) * math.log(p) for p in precisions)
        geo_mean = math.exp(p_log_sum)
    else:
        geo_mean = 0
    
    ratio = float(candidate_length) / reference_length
    if ratio > 1.0:
        bp = 1.
    else:
        bp = math.exp(1 - 1. / ratio)

    bleu = geo_mean * bp


    return (bleu, precisions, bp, ratio, candidate_length, reference_length)


'''
hypothesis = "to make people trustworthy you need to trust them"
reference = "the way to make people trustworthy is to trust them"
bleu, precisions, bp, ratio, candidate_length, reference_length = bleu(hypothesis, reference)
print ("BLEU = ",bleu)
print ("BLEU1 = ",precisions[0])
print ("BLEU2 = ",precisions[1])
print ("BLEU3 = ",precisions[2])
print ("BLEU4 = ",precisions[3])
print ("ratio = ",ratio)
'''