
_beta = 1

def rouge_n(candidate, references, n, alpha=0.5):
    matches = 0
    cand_counts = 0
    for cand_u in candidate:
        cand_u = cand_u.split()
        cand_ngrams = count_ngrams(cand_u, n)
        ref_counts = 0
        cand_counts += len_ngram(cand_ngrams,n)
        for r in references:
            r = r.split()
            r_ngrams = count_ngrams(r, n)
            matches += count_overlap(cand_ngrams, r_ngrams)
            ref_counts += len_ngram(r, n)

    if cand_counts != 0 and ref_counts != 0:
        precision = matches / cand_counts
        recall = matches / ref_counts
        if recall > 1:
            recall = 1
    
    if cand_counts == 0 or ref_counts == 0:
        precision = 0
        recall =0

    f_score = (1 + _beta ** 2) * precision * recall / (recall + _beta ** 2 * precision + 1e-7) + 1e-6 # prevent underflow

    return precision, recall, f_score

def count_ngrams(words, n):
    n_grams_list = []
    for i in range(len_ngram(words, n)):
        n_gram = words[i:i+n]
        n_grams_list.append(n_gram)
    return n_grams_list

def count_overlap(candidate_ngrams, reference_ngrams):
    result = 0
    for w in candidate_ngrams:
        for v in reference_ngrams:
            if w == v:
                result += 1
                break
    return result

def len_ngram(words, n):
    return max(len(words) - n + 1, 0)


