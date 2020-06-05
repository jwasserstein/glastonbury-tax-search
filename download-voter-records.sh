#!/usr/bin/env bash 

cd voter-records
j=()
for i in {1..2653}; do
	j+=("https://voterrecords.com/voters/glastonbury-ct/$i\n")
done
echo -e ${j[@]} | xargs -n 1 -P 10 wget -q
