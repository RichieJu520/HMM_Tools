# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:16:20 2018

@author: jufeng
"""

filename = 'example.domain.tlout'

def hmm_parser(line):
    lis1 = line.rstrip().split(' ')
    lis2 = [x for x in lis1 if x != '']
    return lis2

a={}
b={}
c={}
d={}

i = 0
f=open(filename.replace('.tlout','')+'.besthit.txt','w')
f1=open(filename.replace('.tlout','')+'.ID.txt','w')

for line in open(filename,'r'):
    if line[0]=='#':
        continue
    else:
        lis = hmm_parser(line)
        d[lis[3]] = 1
        if float(lis[5]) <= 0:         #hit filter by bit-score
            i+=1
            continue
        else:
            c[lis[1]]=lis[0]
            try:
                bitsocre = a[lis[2]]
                if float(lis[8]) >= 0.90*bitsocre:
                    #print lis[2]
                    f.write('\t'.join(lis[:18])+'\t'+' '.join(lis[19:(-1)])+'\n')
                else:
                    continue
            except KeyError:
                f.write('\t'.join(lis[:18])+'\t'+' '.join(lis[19:(-1)])+'\n')
                a[lis[2]]=float(lis[8])
                f1.write(lis[3]+ '\n') 
                try:
                    sample_id = b[lis[2].split('_')[0]]
                    f1.write(lis[3]+ '\n') 
                except KeyError:
                    b[lis[3].split('_')[0]]=[lis[1]]
for key in d.keys():
    f1.write(key + '\n')
            
f1.close()
f.close()
print len(c), 'HMM protein families detected!'
print len(a), 'seqeuences annotated'
print len(b), 'samples detected' 