file_name1= "all_complete_Genome_Bac_protein.domain.tlout" ###Enter the full name of .blast file
file_name2= "all_complete_Genome_BacArc_cds.fna" ###Enter the full name of the fasta contains the query sequences

fileinput =open(file_name1,'r')
fileoutput=open(file_name1.replace('.txt','')+'.extracted.fa','w')

print('The Python script is running... Pls wait!')

def hmm_parser(line):
    lis1 = line.rstrip().split(' ')
    lis2 = [x for x in lis1 if x != '']
    return lis2

a={}
m, k=0, 0
for line in open(file_name1,'r'):
    lis = hmm_parser(line)
    m+=1
    try:
        percent = float(lis[5])/float(lis[2])
        if percent < 0.95:
            k+=1
            continue
        else:
            a[lis[3]]=m    ## store query ids as the key of a dic
    except IndexError:
        print(line)
print(len(a),'unique ids in '+file_name1)
print(k + 'alignment with <95% coverage of database domain discarded')


Num, b = 0, []

for line in open(file_name2,'r'):
    
    Num+=1
    if Num%100000==0:
        print(Num, 'sequences have been searched!')
        
    if line.startswith('>'):
        ##ID = str(line.rstrip().split(' ')[0][1:])
        ID = line.rstrip().split('_')[2]  ## a special case
        n = 0
        try:
            j = a[ID]
            fileoutput.write(line)
            n += 1
        except KeyError:
            continue
    else:
        if n == 1:
            fileoutput.write(line)
        else:
            continue

fileinput.close()
print('OK, Finished!')
