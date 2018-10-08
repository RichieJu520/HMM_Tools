# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 17:14:47 2018

@author: jufeng
@email:  jufeng@westlake.edu.cn
written and tested in python 2.7.11

"""

print 'A python script for extracting HMM models using keyword match to HMM name and annotations!'

a={}
i=0

filename1 = 'MGEs_keywrod.v1.txt'
for line in open(filename1,'r'):
    i+=1
    lis =line.rstrip().split('\t')
    a[lis[0].lower()] = lis[1]
print len(a), 'keywords!'

f1 = open(filename1.replace('.txt','')+'_keyword.hmm','w') ## write extracted HMM models
f2 = open(filename1.replace('.txt','')+'_annotation.csv','w') ## write model annotations
f2.write(';'.join(['Model_ID', 'Name', 'Description', 'Keyword', 'Category'])+'\n')

f3=open('example.hmm','r') ## Read HMM model database

model = ''

j, k = 0, 0

while True:
    j +=1
    line = f3.readline()
    if line.strip()!='//':
        if line[:3]=='ACC':
            ID = line[4:].strip().split('.')[0]
            model+=line
        elif line[:4]=='NAME':
            name = line[5:].strip()
            model+=line
        elif line[:4]=='DESC':
            desc = line[5:].strip()
            model+=line
        else:
            model+=line
    else:
        lis = [name] + desc.split(' ')
        for item in lis:
            try:
                b = a[item.lower()]
                f1.write(model)
                f1.write('//'+'\n')
                f2.write(';'.join([ID, name, desc, item, b])+'\n')
                k+=1
                model = ''
                break
            except KeyError:
                continue
        model = ''
                
    if j%100000== 0:
        print j,'lines searched!'
        if line.rstrip() =='':
            break
        
f1.close()
f2.close()
f3.close()
print k, 'models written'
print 'DONE!'

