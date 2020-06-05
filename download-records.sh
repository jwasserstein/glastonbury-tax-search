#!/usr/bin/env bash

rm urls.txt
for j in {1..2653}; do
	echo "https://voterrecords.com/voters/glastonbury-ct/$j" >> urls.txt
done

cd voter-records
cat ../urls.txt | xargs -n 1 -P 10 wget -q
