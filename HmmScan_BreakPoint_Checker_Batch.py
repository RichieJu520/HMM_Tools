# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:52:10 2018

@author: jufeng
"""

import os
import shutil

tloutPath = "domain.tlout_unfinished"
FaaPath = "Fasta1"
SampleList = "sample.txt"

if os.path.exists(SampleList + '_HmmBreakPoints'):
    shutil.rmtree(SampleList+ '_HmmBreakPoints')
os.makedirs(SampleList + '_HmmBreakPoints')


DIC = {}
i = 0
for line in open(SampleList,'r'):
    i += 1
    DIC[line.strip()] = i
    
LIST = DIC.keys()
if i - len(LIST) != 0:
    print (i-len(LIST)), 'redundant IDs ignored!'


def hmm_parser(line):
    lis1 = line.rstrip().split(' ')
    lis2 = [x for x in lis1 if x != '']
    return lis2

for SampleID in LIST:
    
    print "------------------", SampleID, "---------------------"
    
    a = {}
    b = []
    d = []
    
    filename1 = tloutPath + '/'+ SampleID + '.domain.tlout' ## Blast file
    
    for line in open(filename1,'r'):
        if line.startswith('#'):
            d.append(line)
        else:
            lis = hmm_parser(line)
            ID  = lis[3]
            try:
                a[ID] = a[ID] + line
            except KeyError:
                a[ID] =  line
                b.append(ID)
    print len(a)
    
    print 'The blast job breaks at ID: ' + b[-2]
    c = b[:(-2)]   ## discard the last ids
    
    f1 = open(SampleList + '_HmmBreakPoints' + '/' + SampleID + '-1.domain.tlout','w')
    f1.write(''.join(d))
    
    for item in c:
        f1.write(a[item])
        
    f1.close()
    
    filename2 = FaaPath + '/'+ SampleID + '.faa' ## Fasta file
    print 'Extracting unifnished DNA sequences from ID: ' +  b[-2]
    
    i, j, k = 0, 0, 0
    f2 = open(SampleList + '_HmmBreakPoints' + '/' + SampleID+'-2.faa','w')
    
    for line in open(filename2,'r'):
        j += 1
        ID = line[1:].rstrip()
        if ID == b[-2]:
            f2.write(line)
            i+=1
            k+=1
        else:
            if i==1:
                f2.write(line)
                k+=1
            else:
                continue
    print j/2, 'sequences in total'
    print k/2, 'sequences has NOT YET been blasted!'
    print round(float(k)/j, 2)*100, '% unfinished sequences to be continued!'
    f2.close()

print 'DONE!'