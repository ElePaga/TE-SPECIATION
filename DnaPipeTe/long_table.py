import os
import pandas as pd

info = pd.read_csv('../INFO/TABLE11.csv')
print(info)

samples = os.listdir('../busco_metaeuk/')

ks = []

for el in samples:
	k = ''
	for c in el:
		if c != '_':
			k = k + c
		else:
			break
	ks.append(k)

print(ks)
print(len(ks))

def grep_values(TE, srr):
	count_path = srr + '/Counts.txt'
	command = 'grep ' + TE + ' ' + count_path
	line = os.popen(command).read()
	L = line.replace("\n","")
	value_L = L[len(TE)+1:]
	return value_L

cols = ['id', 'specie', 'key', 'TE', '%Genome']
DF = pd.DataFrame(columns = cols)
print(DF)

for smpl in ks:
	if smpl != 'GoA':
		idx = info[info['key']== smpl].index.values
		val = info.iloc[idx]['id']
		val1 = val.tolist()
		val2 = str(val1)
		val3 = val2.replace('[', '')
		val4 = val3.replace(']', '')
		srr = val4[1:len(val4)-1]
		print(srr)
		val_spec = info.iloc[idx]['species']
		val1_spec = val_spec.tolist()
		val2_spec = str(val1_spec)
		val3_spec = val2_spec.replace('[', '')
		val4_spec = val3_spec.replace(']', '')
		spec = val4_spec[1:len(val4_spec)-1]
		print(spec)

		TOT = grep_values('Total', srr)
		print(TOT)
		TE = ['LTR', 'LINE', 'SINE', 'DNA', 'Helitron', 'others', 'na']
		for te in TE:
			elm = grep_values(te, srr)
			print(elm)
			perc = round(int(elm)/int(TOT)*100,2)
			new_row = {'id' : srr, 'specie' : spec, 'key' : smpl, 'TE' : te, '%Genome' : perc}
			DF = pd.concat([DF, pd.DataFrame([new_row])], ignore_index=True)
			print(DF)
	else:
		srr = 'GoA_1-6'
		print(srr)
		TOT = grep_values('Total', srr)
		print(TOT)
		TE = ['LTR', 'LINE', 'SINE', 'DNA', 'Helitron', 'others', 'na']
		for te in TE:
			elm = grep_values(te, srr)
			print(elm)
			perc = round(int(elm)/int(TOT)*100,2)
			new_row = {'id' : srr, 'specie' : spec, 'key' : smpl, 'TE' : te, '%Genome' : perc}
			DF = pd.concat([DF, pd.DataFrame([new_row])], ignore_index=True)
			print(DF)

DF.to_csv('TEspec.csv', index = False)
