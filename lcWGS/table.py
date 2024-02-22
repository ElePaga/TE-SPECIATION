import pandas as pd

dic = {}

df_entries = pd.read_csv("../DatasetCreation/sra_paired_clean.csv", header = None)
print(df_entries)

df_srr = pd.read_csv("../DatasetCreation/SRRcode.csv", header = None)

idx = 0
for el in df_srr[0]:
	dic[el] = df_entries[2][idx]
	idx += 1

print(dic)

