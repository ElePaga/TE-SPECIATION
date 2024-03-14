import subprocess

f = '../clean_assemblies/SRR15979864_output_clean.fasta'
f_old = open(f,'r')

command = 'touch ../PROVA/SRR15979864_correct_clean.fasta'
subprocess.call(command, shell=True)

f_c = '../PROVA/SRR15979864_correct_clean.fasta'
f_correct = open(f_c, 'a')

for line in f_old:
	if line[0] == '>':
		f_correct.write(line)
	else:
		idx = 1
		l = ''
		for el in line:
			if idx != 61 and el != '\n':
				l = l + el
				idx += 1
			else:
				l = l +'\n'
				if len(l) != 1:
					f_correct.write(l)
				idx = 2
				l = el

f_correct.close()
