# Run in taxid conda env

import os
import pandas as pd
import subprocess

srr_df = pd.read_csv("DatasetCreation/SRRcode.csv", header=None)

srr_l = srr_df[0].tolist()
print(srr_l)


col = ['SRR','BioSample','sex']

INFO = pd.DataFrame(columns=col)

INFO['SRR'] = srr_l

print(INFO)

idx = 0
for srr in srr_l:
	command = 'bionode-ncbi search sra ' + srr +' --pretty | grep "Biosample"'
	biosample = os.popen(command).read()
	print(biosample)
	bios = biosample[18:len(biosample)-2]
	print(bios)
	INFO.loc[idx, 'BioSample'] = bios
	idx += 1


print(INFO)

bio_l = INFO['BioSample']

idx1 = 0
for bs in bio_l:
        command = 'bionode-ncbi search biosample ' + bs + ' --pretty | grep -e "female" -e "male"'
        sex = os.popen(command).read()
        print(sex)
        s = sex[18:len(sex)-3]
        print(s)
        INFO.loc[idx1, 'sex'] = s
        idx1 += 1

print(INFO)

INFO.to_csv('INFO.csv')
