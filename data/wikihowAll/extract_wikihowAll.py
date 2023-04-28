import pandas as pd
import os
import re
import summa
from summa import summarizer

# read data from the csv file 
Data = pd.read_csv(r'data/wikihowAll/wikihowAll.csv')
Data = Data.astype(str)
rows, columns = Data.shape

 
title_file = open('data/wikihowAll/titles.txt', 'wb')

path_a = "data/wikihowAll/systems"
if not os.path.exists(path_a): os.makedirs(path_a)

path_s = "data/wikihowAll/summaries"
if not os.path.exists(path_s): os.makedirs(path_s)


for row in range(rows):

    abstract = Data.iloc[row,Data.columns.get_loc('headline')]      
    article = Data.iloc[row,Data.columns.get_loc('text')]          
    # a threshold is used to remove short articles with long summaries as well as articles with no summary
    if len(abstract) < (0.75*len(article)):
        # remove extra commas 
        abstract = abstract.replace(".,",".")
        abstract = abstract.encode('utf-8')
        article = re.sub(r'[.]+[\n]+[,]',".\n", article)
        article = article.encode('utf-8')
        
        '''
        with open('data/temporaryFile.txt','wb') as t:
            t.write(abstract)
        
        '''
        # store file names 
        filename = Data.iloc[row,Data.columns.get_loc('title')]
        filename = "".join(x for x in filename if x.isalnum())
        filename1 = filename + '.txt'
        filename = filename.encode('utf-8')
        title_file.write(filename+b'\n')
        
        with open(path_a+'/'+filename1,'wb') as f:   
            # store articles
            article = article.decode('utf-8')
            system = summarizer.summarize(article)
            system = system.encode('utf-8')
            f.write(system)
        
        with open(path_s+'/'+filename1,'wb') as f:
            # store summary
            f.write(abstract)
            '''
            with open('data/temporaryFile.txt','r') as t:
                for line in t:
                    line=line.lower()
                    if line != "\n" and line != "\t" and line != " ":
                        f.write(line.encode('utf-8'))
            '''
                    
        


title_file.close()

    
