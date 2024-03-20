import subprocess
import os
import sys 

if  __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Wrong call')
		sys.exit()
	f_c = sys.argv[1]
	f_rm = sys.argv[2]


sample = 'SRR'
for c in f_c:
	if c in ['0','1','2','3','4','5','6','7','8','9']:
		sample = sample + c

file_rm = open(f_rm, 'r')
file_c = open(f_c, 'r')


# OBTAIN THE LIST OPF CONTIGS

nodes_all = []
for line in file_c:
        node = ''
        if line[0] == '>':
                for el in line:
                        if el != ' ':
                                node = node + el
                        else:
                                break
                if node[len(node)-1] != '\n':
                        node = node + '\n'
                nodes_all.append(node[1:])
print(nodes_all)
print('-' * 30)

# OBTAIN THE LIST OF CONTAMINANT CONTIGS 

nodes_to_rm = []
for line in file_rm:
	node = ''
	if line[0] == '>':
		for el in line:
			if el != ' ':
				node = node + el
			else:
				break
		if node[len(node)-1] != '\n':
			node = node + '\n'
		nodes_to_rm.append(node[1:])
print(nodes_to_rm)
print('-' * 30)


# CREATE THE FILE WITH THE LIST OF CONTIGS TO KEEP

nodes_clean = []
for c in nodes_all:
	if c not in nodes_to_rm:
		nodes_clean.append(c)

print(nodes_clean)
#c_l = '../clean_assemblies/' + sample + '_contig_list.csv'
c_l = '../PROVA/' + sample + '_contig_list.csv'
contigs_list = open(c_l, 'w+')
for cont in range(len(nodes_clean)):
	contigs_list.write(nodes_clean[cont])


file_rm.close()
file_c.close()
contigs_list.close()

command = 'seqtk subseq ' + f_c + ' ' + c_l + ' > ../clean_assemblies/' + sample + '_output_clean.fasta'
#command = 'seqtk subseq ' + f_c + ' ' + c_l + ' > ../PROVA/' + sample + '_output_clean.fasta'
subprocess.call(command, shell=True)


