import os
import subprocess
import pandas as pd

dir = os.listdir('../minimap_out')
print(dir)
df = pd.read_csv('../g_size/respect/gsize_clean.csv')
print(df)
counter = 0

for el in dir:

	counter += 1
	print(counter)

	reads = el + '.clean_1.fastq'
	print(reads)
	path_reads = '../minimap_out/' + el + '/' + reads
	print(path_reads)
	library = 'ALL_MCHelper_Ants_TEs.renamed.SubFam.fa'
	specie = el
	row_index = df.index[df['sample'] == reads].tolist()
	gsize_l = df['genome_length'].values[row_index]
	g_size = str(gsize_l[0])
	print(g_size)

	command_dpt = 'bash dnapipete.sh ' + path_reads + ' ' + library + ' ' +  specie + ' ' + g_size
	print(command_dpt)
#	subprocess.call(command_dpt, shell = True)
	command_rm = 'rm ' + reads
	print(command_rm)
#	subpricess.call(command_rm, shell = True)
