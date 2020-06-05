#!/usr/bin/env bash

cd voter-records

rm urls.txt
for j in {1..2653}; do
	echo "https://voterrecords.com/voters/glastonbury-ct/$j" >> urls.txt
done

cat urls.txt | xargs -n 1 -P 10 wget -q
