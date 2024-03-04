file_rm = open('PROVA_SRR15979878_ToRemove.fasta', 'r')
file_c = open('PROVA_SRR15979878_contigs.fasta', 'r')

#file_rm = open('prova_toremove.fasta', 'r')
#file_c = open('prova_contig.fasta', 'r')

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
		nodes_to_rm.append(node)
print(nodes_to_rm)
print('-' * 30)


Lines = file_c.readlines()
idx = 0
print(Lines)

while idx != len(Lines):
	if Lines[idx] in nodes_to_rm:
		nodes_to_rm.remove(Lines[idx])
		Lines.remove(Lines[idx])
		while True:
			if Lines[idx][0] != '>':
				Lines.remove(Lines[idx])
			else:
				print(Lines[idx])
				idx -= 1
				break
	idx += 1

'''
for line in Lines:
	if line in nodes_to_rm:
		Lines.remove(line)
		while True:
			if Lines[idx][0] != '>':
				Lines.remove(Lines[idx])
			else:
				break
	else:
		idx += 1

'''

#f_clean = open ('prova_clean_contigs.fasta', 'w+')
f_clean = open('PROVA_SRR15979878_clean.fasta', 'w+')

for l in range(len(Lines)):
	f_clean.write(Lines[l])


file_rm.close()
file_c.close()
f_clean.close()
