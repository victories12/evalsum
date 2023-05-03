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
 '''python
 1
 '''
 
