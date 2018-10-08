# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 17:14:47 2018

@author: jufeng
@email:  jufeng@westlake.edu.cn
written and tested in python 2.7.11

"""


print 'A python script for extracting HMM models using IDs!'


i=0
ID_dic = {}

filename = 'ID.txt'
for line in open(filename,'r'):
    i+=1
    try:
        j = ID_dic[line.strip().split('\t')[0]]
        print line
    except KeyError:
        ID_dic[line.strip().split('\t')[0]] = i
    
print i,'model ids to be extracted!'
print len(ID_dic),'unique model ids!'

f=open('example.hmm','r')
f1 = open(filename.replace('.txt','')+'.hmm','w')
model = ''

j, k = 0, 0
while True:
    j +=1
    line = f.readline()
    if line.strip()!='//':
        if line[:3]=='ACC':
            ID = line[4:].strip().split('.')[0]
            model+=line
        else:
            model+=line
    else:
        try:
            b = ID_dic[ID]
            f1.write(model)
            f1.write('//'+'\n')
            k+=1
            model = ''
        except KeyError:
            model = ''
            continue
    if j%1000000== 0:
        print j,'lines searched!'
        if line.rstrip() =='':
            break
print k, 'models written'

f.close()
f1.close()
print 'DONE!'