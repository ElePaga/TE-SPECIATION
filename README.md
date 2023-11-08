# TE-SPECIATION

## Dataset Creation from NCBI 

The first dataset was retrieved from RSA using _formica_ as search world and _paired_ as filter. The summary of the 3,444 entries was downloaded as a text file (**sra_result_paired.txt**).
The dataset was then filtered based on some keywords associated to features we weren't interested in, those words are reported in the file **keywordsrmv.txt**.
The final file **sra_paired_clean.txt** was genered through the command line:
```shell
grep -vi -f keywordsrmv.txt sra_paired_results.txt > sra_paired_clean.txt
```
Then, a file containing the remaining selected organisms with associated the amount of available entries for each of them was generated (**species.txt**):
```shell
cut -f 3 -d "," sra_paired_clean.txt | sort | uniq -c | sort -nkr 1 > species.txt
```

The SRX code (associated to each experiment) was used to retrive the SRR code required for the download of each set of reads. To do so
 the **retrieveSRRcode.py** code was used and the **SRRcode.csv** was generated. 

Once the SRR codes were retrieved, they were used to download the fastq files containing the reads.
The _SRAtoolkit_ was used to download the files in sra format and then convert them into fastq files (the combo _prefetch_ + _fasterq-dump_ should
make the process faster than using directly fastq-dump).
The **downloadSRA.py** (in _SRAfiles/_) code was used to do so and generate a directory _fastq/_ containing a folder for each SRR with inside the 2
fastq files (paired ends).
