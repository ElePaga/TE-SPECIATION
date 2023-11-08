import pandas as pd
import subprocess
from csv import writer

# RETRIEVE SRX CODE (experiment accession)
df_entries = pd.read_csv("sra_paired_clean.csv", header = None)

SRX_values = df_entries[0].values
print(SRX_values)

# RETRIEVE SRR CODE (run accession)
for code in SRX_values:
	print("Retriving sra ID for: " + code)
	# Esearch is used to access the sra database (-db sra) using as a query the experiment accession
	# Efetch is used to obtain a file with the info associated to such experiment
	# The first column of the file containing the run accession is saved into SRR.csv
	convert = "esearch -db sra -query " + code + " | efetch -format runinfo | cut -d ',' -f 1 > SRR.csv"
	print("The command used was: " + convert)
	subprocess.call(convert, shell=True)

	# The run accession is retrieved
	df_srr = pd.read_csv("SRR.csv")
	print(df_srr)
	id = df_srr["Run"].values[0]
	print(id)

	# The run accession is appended to an existing SRRcode.csv file
	# The SRRcode.csv was created previously the run as an empty file
	with open("SRRcode.csv", "a") as f_object:
		row_g = [id]
		writer_object = writer(f_object)
		writer_object.writerows([row_g])
		f_object.close()

