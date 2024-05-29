#!/bin/bash


READS=$( realpath "$1")
TE_LIB=$( realpath "$2")
SPECIE="$3"
GENOME_SIZE="$4"


#cp "$TE_LIB" .
cp "$READS" .


READS_BASE=$(basename "$READS")
TE_LIB_BASE=$(basename "$TE_LIB")



echo -e "#! /bin/bash" > Commands/"$SPECIE"_dnaPT_cmd.sh
echo -e "python3 dnaPipeTE.py -input /mnt/$READS_BASE -sample_number 2 -output /mnt/${SPECIE} -RM_lib /mnt/$TE_LIB_BASE -genome_size $GENOME_SIZE -genome_coverage 0.2 -sample_number 2 -RM_t 0.2 -cpu 5" >> Commands/"$SPECIE"_dnaPT_cmd.sh
chmod +x Commands/"$SPECIE"_dnaPT_cmd.sh
docker run -v $(pwd):/mnt clemgoub/dnapipete:latest /mnt/Commands/"$SPECIE"_dnaPT_cmd.sh
