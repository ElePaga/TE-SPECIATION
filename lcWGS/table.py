import pandas as pd
import os
import subprocess

dic = {}

df_entries = pd.read_csv("../DatasetCreation/sra_paired_clean.csv", header = None)
print(df_entries)

df_srr = pd.read_csv("../DatasetCreation/SRRcode.csv", header = None)


idx = 0
for el in df_srr[0]:
	dic[el] = df_entries[2][idx]
	idx += 1


print(dic)


samples_list = os.listdir("../DatasetCreation/SRAfiles/fastq/")
#print(samples_list)

columns = ['id','species']

TABLE = pd.DataFrame(columns=columns)

missing = []
k = list(dic.keys())
print(k)

print(len(k))

'''
for id in k:
	if id not in samples_list:
		missing.append(id)

TABLE['id'] = missing

idx0 = 0
for el in missing:
        value = dic[el]
        TABLE.loc[idx0, "species"] = value
        idx0 += 1

print(TABLE)

TABLE.to_csv('missing.csv')
'''

samples_list = os.listdir("../DatasetCreation/SRAfiles/fastq/")
print(samples_list)

columns = ['id','species','#reads_downloaded','#reads_before','#reads_after','#contigs_before','#contigs_after','genome_size']

TABLE = pd.DataFrame(columns=columns)


TABLE['id'] = k


#contigs_before
idx1 = 0
for el in k:
	value = dic[el]
	TABLE.loc[idx1, "species"] = value
	idx1 += 1


print(TABLE)

idx2 = 0
for el in k:
	print('1_' + str(idx2))
	if el in samples_list:
		grep = "grep -c '@' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".sra_1.fastq"
		n = os.popen(grep).read()
	else:
		grep = "grep -c '@' ../DatasetCreation/pending_sra/" + el + "/" + el + ".sra_1.fastq"
		n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx2, '#reads_downloaded'] = val
	idx2 += 1


idx3 = 0
for el in k:
	print('2_' + str(idx3))
	if el in samples_list:
		grep = "grep -c '@' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".trimmed_1P.fq"
		n = os.popen(grep).read()
	else:
		grep = "grep -c '@' ../DatasetCreation/pending_sra/" + el + "/" + el + ".sra_1.fastq"
		n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx3, '#reads_before'] = val
	idx3 += 1


'''
idx4 = 0
for el in k:
	print('3_' + str(idx4))
	grep = "grep -c '@' ../minimap_out/" + el + "/" + el + ".clean_1.fastq"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx4, '#reads_after'] = val
	idx4 += 1
'''

idx5 = 0
for el in k:
	print('4_' + str(idx5))
	grep = "grep -c '>' ../assemblies/" + el + "_spades/contigs.fasta"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx5, '#contigs_before'] = val
	idx5 += 1


idx6 = 0
for el in k:
	print('5_' + str(idx6))
	grep = "grep -c '>' ../clean_assemblies/" + el + "_output_clean.fasta"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx6, '#contigs_after'] = val
	idx6 += 1

print(TABLE)

TABLE.to_csv('TABLE.csv')

