import subprocess
import pandas as pd

# ACCESS THE SRR CODE FOR EACH READS FILE 
df_srr = pd.read_csv("SRRcode.csv", header=None)
sra_numbers= df_srr[0].values
#sra_numbers = ['SRR15979786', 'SRR15979787', 'SRR15979789', 'SRR15979790', 'SRR15979791', 'SRR15979792', 'SRR15979794', 'SRR15979795', 'SRR15979796', 'SRR15979797', 'SRR15979800', 'SRR15979801', 'SRR15979802', 'SRR15979803', 'SRR15979804', 'SRR15979805', 'SRR15979806', 'SRR15979807', 'SRR15979808', 'SRR15979809', 'SRR15979810', 'SRR15979811', 'SRR15979812', 'SRR15979813', 'SRR15979814', 'SRR15979815', 'SRR15979816', 'SRR15979817', 'SRR15979818', 'SRR15979819', 'SRR15979820', 'SRR15979821', 'SRR15979822', 'SRR15979823', 'SRR15979824', 'SRR15979825', 'SRR15979826', 'SRR15979827', 'SRR15979828', 'SRR15979829', 'SRR15979830', 'SRR15979831', 'SRR15979832', 'SRR15979833', 'SRR15979834', 'SRR15979835', 'SRR15979836', 'SRR15979837', 'SRR15979838', 'SRR15979839', 'SRR15979842', 'SRR15979844', 'SRR15979845', 'SRR15979846', 'SRR15979847', 'SRR15979848', 'SRR15979850', 'SRR15979851', 'SRR15979852', 'SRR15979853', 'SRR15979854', 'SRR15979855', 'SRR15979857', 'SRR15979858', 'SRR15979859', 'SRR15979860', 'SRR15979861', 'SRR15979862', 'SRR15979863', 'SRR15979864', 'SRR15979865', 'SRR15979866', 'SRR15979867', 'SRR15979868', 'SRR15979869', 'SRR15979870', 'SRR15979871', 'SRR15979872', 'SRR15979873', 'SRR15979874', 'SRR15979875', 'SRR15979876', 'SRR15979877', 'SRR15979878', 'SRR15979879', 'SRR15845610', 'SRR15845621', 'SRR15845632', 'SRR15845271', 'SRR15845282', 'SRR15845293', 'SRR15845377', 'SRR15845476', 'SRR15845487', 'SRR15845488', 'SRR15845499', 'SRR15845510', 'SRR15845521', 'SRR15845526', 'SRR15845527', 'SRR15845528', 'SRR15845536', 'SRR15845547', 'SRR15845558', 'SRR15845569', 'SRR15845580', 'SRR15845591']
print(sra_numbers)

# DOWNLOAD THE READS FROM SRA
genome_n = 1
for sra_id in sra_numbers:
	print(genome_n)
	genome_n += 1 
	print("Currently downloading: " + sra_id)
	prefetch = "prefetch " + sra_id
	# The prefetch command download the reads file in SRA format
	print("The command used was: " + prefetch)
	subprocess.call(prefetch, shell=True)

# GENERATING FASTQ FILES
genome_n2 = 1
for sra_id in sra_numbers:
	print(genome_n2)
	genome_n2 += 1
	print("Generating fastq for: " + sra_id)
	# Fasterq-dump converts the SRA file into fastq files and move them to the fastq/ dir
	# A folder is created for each SRA file containing the 2 corresponding fastq files (paired ends)
	fasterq_dump = "fasterq-dump --outdir fastq/" + sra_id + " ~/TE-SPECIATION/SRAfiles/" + sra_id + "/" + sra_id + ".sra" 
	print("The command used was: " + fasterq_dump)
	subprocess.call(fasterq_dump, shell=True)
	# Once the fastq files have been generated, the SRA files are deleted to avoid occupying too much space
	rm_sra = "rm -r " + sra_id
	print("The command used was: " + rm_sra)
	subprocess.call(rm_sra, shell=True)

