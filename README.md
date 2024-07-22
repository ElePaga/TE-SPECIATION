# TE-SPECIATION
## Dataset Creation from NCBI 

The first dataset was retrieved from RSA using _formica_ as search world and _paired_ as filter. The summary of the 3,444 entries was downloaded as a text file (**sra_result_paired.txt**).
The dataset was then filtered based on some keywords associated to features we weren't interested in, those words are reported in the file **keywordsrmv.txt**.
The final file **sra_paired_clean.txt** was genered through the command line:
```shell
grep -vi -f keywordsrmv.txt sra_paired_results.txt > sra_paired_clean.txt
```
Then, a file containing the remaining selected organisms with associated the amount of available runs for each of them was generated (**species.txt**):
```shell
cut -f 3 -d "," sra_paired_clean.txt | sort | uniq -c | sort -nrk 1 > species.txt
```

The SRX code (associated to each experiment) was used to retrive the SRR code required for the download of each set of reads. To do so
the **retrieveSRRcode.py** code was used and the **SRRcode.csv** was generated. 

Once the SRR codes were retrieved, they were used to download the fastq files containing the reads.
The _SRAtoolkit_ was used to download the files in sra format and then convert them into fastq files through the combo _prefetch_ + _fasterq-dump_.
The **downloadSRA.py** code was used to do so and generate a directory _fastq/_ containing a folder for each SRR with inside the 2
fastq files (paired ends).


## lcWGS snakemake pipeline

The directory _lcWGS_ contains the **snakefile** for the run of the lcWGS pipeline (for the analysis of low coverage WGS reads), to run the file the snakemake environment needs to be activated (**environment_snakemake.yml**).
What is more, the conda environments to run _mitoz_ and _busco_ are required (**environment_mitoz.yml**, **environment_busco.yml**).
In addition, the following sripts/libraries need to be installed: **fcs.py** (https://github.com/ncbi/fcs-gx), **minimap2** (https://github.com/lh3/minimap2),
**samtools** (https://github.com/samtools/samtools?tab=readme-ov-file), **RESPECT** (https://github.com/shahab-sarmashghi/RESPECT, activating the **respect_environment.yml**).
**NB.** Path to some of the above scripts/libraries might be adjusted based on the download folders and the threads need to be adjusted based on the computer availability. 

To perform the dryrun of the code it can be used the following command line:
```shell 
snakemake --cores 4 --verbose -p --rerun-incomplete --keep-going --use-conda  -n
```

To fully execute the snakefile it was used the following command line:
```shell 
snakemake --cores 4 --verbose -p --rerun-incomplete --keep-going --use-conda
```

To run only up to specific rule '-U _RuleName_' can be added to the command line.

The pipeline output is reported in INFO/TABLE11.csv.


## INFO folder

The INFO folder contains scripts and tables with the information of the datasets and the outputs of the lcWGS pipeline.

Particularly, the TABLE11.csv was generated with **complete_table.py** script 
and it contains the data retrieved through the lcWGS pipeline and others, in order:  
-id -> The SRR code  
-species -> The sample specie  
-key -> The key associated to each sample  
-#reads_downloaded -> The number of reads downloaded from SRA  
-#reads_before -> The number of reads resulting from the trimming process  
-#reads_clean -> The number of reads at the end of the lcWGS pipeline (all the reads excluded the contaminant and mitochondrial ones)  
-#contigs_before -> The number of contigs assempled by Spades  
-#contigs_clean -> The number of contigs exluding the contaminant and mitochondrial ones  
-genome_size -> The estimated genome size by RESPECT in terms of bp  
-coverage -> The estimated coverage by RESPECT  
-busco -> The busco output  

To run the **sample_info.py** script the **environment_info.yml** needs to be activated.


## dnaPipeTE

The dnaPipeTE pipeline was used to identify the transposable elements in the genome starting from the reads and the genome size.
The **RunDnapipete.py** script is used to run dnaPipeTE over all the samples and it calls the **bash dnapipete.sh** script that executes dnaPipeTE.
In order to run everything the reads non-trimmed and clean from contaminants and mitochondrial reads are required, together with the genome size (INFO/gsize_clean.csv)
and the TEs library **ALL_MCHelper_Ants_TEs.renamed.SubFam.fa** (info are on the DnaPipeTe/README.txt).  
The most relevant ouputs for each sample are uploaded in the specific folder in DnaPipeTe/.

## Formica phylogeny 




