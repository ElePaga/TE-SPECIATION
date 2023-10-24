# TE-SPECIATION

## Dataset from NCBI 

The first dataset was retrieved from RSA using _formica_ as search world and _paired_ as filter. The summury of the 3,444 entries was downloaded as a text file (**sra_result_paired.txt**).
The dataset was then filtered based on some keywords associated to features we weren't interested in, those words are reported in the file **keywordsrmv.txt**.
The final file **sra_paired_clean.txt** was genered through the command line:
```shell
grep -vi -f keywordsrmv.txt sra_paired_results.txt > sra_paired_clean.txt
```
Then, a file containing the remaining selected organisms with associated the amount of available entries for it was generated (**species.txt**):
```shell
cut -f 3 -d "," sra_paired_clean.txt | sort | uniq -c | sort -nkr 1 > species.txt
```
