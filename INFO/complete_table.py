import pandas as pd
import numpy as np
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

DF = pd.DataFrame(columns=columns)
srr = list(dic.keys())
print(srr)
print(len(srr))

samples_list = os.listdir("../DatasetCreation/SRAfiles/fastq/")
print(samples_list)

columns = ['id','species', 'key', '#reads_downloaded','#reads_before','#reads_clean','#contigs_before','#contigs_clean','genome_size',
	'coverage', 'busco']

DF = pd.DataFrame(columns=columns)


DF['id'] = srr

indx = 0
for el in srr:
	value = dic[el]
	DF.loc[indx, "species"] = value
	indx += 1


print(DF)

# READS DOWNLOADED
idx1 = 0
for el in srr:
	print('1_' + str(idx1))
	grep = "grep -c '@' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".sra_1.fastq"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	DF.loc[idx1, '#reads_downloaded'] = val
	idx1 += 1

# READS BEFORE
idx2 = 0
for el in srr:
	print('2_' + str(idx2))
	grep = "grep -c '@' ../DatasetCreation/SRAfiles/fastq/" + el + "/" + el + ".trimmed_1P.fq"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	DF.loc[idx2, '#reads_before'] = val
	idx2 += 1

# READS CLEAN
idx3 = 0
for el in srr:
        print('3_' + str(idx3))
        grep = "grep -c '@' ../minimap_out/" + el + "/" + el + ".clean_1.fastq"
        n = os.popen(grep).read()
        number = n.replace("\n","")
        dic[el] = number
        val = dic[el]
        DF.loc[idx3, '#reads_clean'] = val
        idx3 += 1

# CONTIGS BEFORE
idx4 = 0
for el in srr:
	print('4_' + str(idx4))
	grep = "grep -c '>' ../assemblies/" + el + "_spades/contigs.fasta"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	DF.loc[idx4, '#contigs_before'] = val
	idx4 += 1

# CONTIGS CLEAN
idx5 = 0
for el in srr:
	print('5_' + str(idx5))
	grep = "grep -c '>' ../clean_assemblies/" + el + "_output_clean.fasta"
	n = os.popen(grep).read()
	number = n.replace("\n","")
	dic[el] = number
	val = dic[el]
	DF.loc[idx5, '#contigs_clean'] = val
	idx5 += 1


df_gsize = pd.read_csv('g_size.csv')

for el in df_gsize['sample']:
	print(el)
	df_gsize.replace(el, el[:11], inplace=True)

print(df_gsize)

idx6 = 0
for el in srr:
	i = df_gsize[df_gsize['sample'] == el].index.values
	gs = df_gsize.iloc[i]['genome_length']
	val = gs.tolist()
	val2 = str(val)
	val3 = val2.replace('[', '')
	val4 = val3.replace(']', '')
	DF.loc[idx6, 'genome_size'] = val4
	idx6 += 1

idx7 = 0
for el in srr:
        i = df_gsize[df_gsize['sample'] == el].index.values
        gs = df_gsize.iloc[i]['coverage']
        val = gs.tolist()
        val2 = str(val)
        val3 = val2.replace('[', '')
        val4 = val3.replace(']', '')
        DF.loc[idx7, 'coverage'] = val4
        idx7 += 1


df_busco = pd.read_csv('keys.csv')
print(df_busco)

dic_busco = df_busco.set_index('key').T.to_dict('list')
print(dic_busco)

path = '../busco_out/'
dir_busco = os.listdir(path)
print(dir_busco)

for elm in dir_busco:
	k = ''
	for char in elm:
		if char != '_':
			k = k + char
		else :
			break
	command1 = "grep 'C:' ../busco_out/" + elm + "/short_summary.specific.metazoa_odb10." + dic_busco[k][0] + "_busco.txt"
	value =  os.popen(command1).read()
	value = value.replace('\t', '')
	value = value.replace('\n', '')
	i_busco = DF[DF['id']== dic_busco[k][0]].index.values
	DF.loc[i_busco, 'key'] = k
	DF.loc[i_busco, 'busco'] = value

print(DF)

DF.to_csv('FINAL_TABLE', index = False)

