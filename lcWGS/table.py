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
print(samples_list)

columns = ['id','species','#reads_before1','#reads_after1', '#reads_before2','#reads_after2','n_size','genome_size']

TABLE = pd.DataFrame(columns=columns)


TABLE['id'] = samples_list

idx = 0
for el in samples_list:
	value = dic[el]
	TABLE.loc[idx, "species"] = value
	idx += 1

idx2 = 0
for el in samples_list:
	grep = "grep -c '+' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".trimmed_1P.fq"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx2, '#reads_before1'] = val
	idx2 += 1

idx3 = 0
for el in samples_list:
	grep = "grep -c '+' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".trimmed_2P.fq"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	TABLE.loc[idx3, '#reads_before2'] = val
	idx3 += 1



print(TABLE)

