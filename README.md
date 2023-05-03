# evalsum
Re-implement rouge_l, rouge_n, bleu using python. Test them on datasets wikihowAll and DUC2002. Fork me if you like my method.


## Project File Structure

📦project<br>
 ┣ 📂data<br>
 ┃ ┣ 📂DUC2002 --> Store candidate summaries and reference summaries on DUC 2002 <br>
 ┃ ┃   ┣ 📂candidates --> Store candidates summaries<br>
 ┃ ┃   ┣ 📂referenceA --> Store No.1 group of reference summaries<br>
 ┃ ┃   ┗ 📂referenceB --> Store No.2 group of reference summaries<br>
 ┃ ┗ 📂wikihowAll --> Store wikihow dataset <br>
 ┃ ┃    ┣ extract_wikihowAll.py --> If you want to store the articles and reference summaries here, run this file. Or you could skip this.<br>
 ┃ ┃    ┗ wikihowAll.csv --> Download from the link and store it here.<br> 
 ┃ <br>
 ┣ 📂metrics <br>
 ┃ ┣ bleu.py --> BLEU metric <br>
 ┃ ┣ rouge_l.py --> ROUGE-L metric <br>
 ┃ ┗ rouge_n.py --> ROUGE-N metric<br>
 ┃ <br>
 ┣ 📂results --> external tools<br>
 ┃ ┣ 📂DUC2002 --> models for object detection<br>
 ┃ ┃ ┃<br>
 ┃ ┃ ┣ 📂A --> Store scores for N0.1 group reference summaries and candidate summaries on DUC 2002<br>
 ┃ ┃ ┃ ┣ BLEU.csv --> Record BLEU scores<br>
 ┃ ┃ ┃ ┣ ROUGE_1.csv --> Record ROUGE_1 scores<br>
 ┃ ┃ ┃ ┣ ROUGE_2.csv --> Record ROUGE_2 scores<br>
 ┃ ┃ ┃ ┗ ROUGE_L.csv --> Record ROUGE_L scores<br>
 ┃ ┃ ┃<br>
 ┃ ┃ ┗ 📂B --> Store scores for N0.2 group reference summaries and candidate summaries on DUC 2002<br>
 ┃ ┃ ┃ ┣ BLEU.csv<br>
 ┃ ┃ ┃ ┣ ROUGE_1.csv <br>
 ┃ ┃ ┃ ┣ ROUGE_2.csv<br>
 ┃ ┃ ┃ ┗ ROUGE_L.csv <br>
 ┃ ┃ ┃<br>
 ┃ ┃ ┣ 📂wikihowAll --> Store scores for wikihow dataset <br>
 ┃ ┃ ┃ ┣ BLEU.csv<br>
 ┃ ┃ ┃ ┣ ROUGE_1.csv<br>
 ┃ ┃ ┃ ┣ ROUGE_2.csv <br>
 ┃ ┃ ┃ ┗ ROUGE_L.csv<br>
 ┃<br>
 ┣ compare_metrics.py --> Compare between the results of my metrics with the metrics from other package.<br>
 ┣ demo.py --> Test metrics using very simple example to help you understand.<br>
 ┣ run_DUC.py --> Use metrics to evaluate summaries on DUC 2002. The outputs will be stored in results directory. <br>
 ┗ run_wikihowAll.py --> Use metrics to evaluate summaries on wikihow.The outputs will be stored in results directory. <br>
 
 ## How to use it
 -check example in the demo.py
```python
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
``` 

## Test on dataset
-Run run_DUC.py to test metrics on DUC 2002 dataset

-Run run_wikihowAll.py to test metrics on wikihow dataset. Before running, please download wikihowAll.csv from https://ucsb.box.com/s/ap23l8gafpezf4tq3wapr6u8241zz358 and put it to path /data/wikihowAll.
