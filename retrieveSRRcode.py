import pandas as pd
import subprocess
from csv import writer

df_entries = pd.read_csv("sra_paired_clean.csv", header = None)

SRX_values = df_entries[0].values
print(SRX_values)


for code in SRX_values:
	print("Retriving sra ID for: " + code)
	convert = "esearch -db sra -query " + code + " | efetch -format runinfo | cut -d ',' -f 1 > SRR.csv"
	print("The command used was: " + convert)
	subprocess.call(convert, shell=True)

	df_srr = pd.read_csv("SRR.csv")
	print(df_srr)
	id = df_srr["Run"].values[0]
	print(id)

	with open("SRRcode.csv", "a") as f_object:
		row_g = [id]
		writer_object = writer(f_object)
		writer_object.writerows([row_g])
		f_object.close()

