
_beta = 1
# The longest common subsequence in Python
# Function to find lcs
def lcs(S1, S2):
    m = len(S1)
    n = len(S2)
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    return index


def rouge_l(candidate, reference):
    
    lcs_score = 0
    #print(candidate)
    #print("\n")
    #print(reference)
    for cand_u in candidate:
        matches = []
        for ref_u in reference:
            matches.append(lcs(cand_u,ref_u)) 
        lcs_score += max(matches)
      

    ref_counts = sum(len(s) for s in reference)
    cand_counts = sum(len(s) for s in candidate)

    if cand_counts != 0 and ref_counts != 0:
        precision = lcs_score / cand_counts
        recall = lcs_score / ref_counts
    
    if cand_counts == 0 or ref_counts == 0:
        precision = 0
        recall =0
    
    f_score = (1 + _beta ** 2) * precision * recall / (recall + _beta ** 2 * precision + 1e-7) + 1e-6 # prevent underflow

    return precision, recall, f_score

'''
text = "The Kyrgyz President pushed through the law requiring the use of ink during the upcoming Parliamentary and Presidential elections In an effort to live up to its reputation in the 1990s as an island of democracy. The use of ink is one part of a general effort to show commitment towards more open elections. improper use of this type of ink can cause additional problems as the elections in Afghanistan showed. The use of ink and readers by itself is not a panacea for election ills."
ref = "The use of invisible ink and ultraviolet readers in the elections of the Kyrgyz Republic which is a small, mountainous state of the former Soviet republic, causing both worries and guarded optimism among different sectors of the population. Though the actual technology behind the ink is not complicated, the presence of ultraviolet light (of the kind used to verify money) causes the ink to glow with a neon yellow light. But, this use of the new technology has caused a lot of problems. "

rouge_l = rouge_l(
            [text],
            [ref])
print(rouge_l)
'''