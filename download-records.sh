#!/usr/bin/env bash 

cd voter-records
for i in {1..3}; do
	j="$j\nhttps://voterrecords.com/voters/glastonbury-ct/$i"
done
echo -e $j | xargs -n 1 -P 10 wget 
