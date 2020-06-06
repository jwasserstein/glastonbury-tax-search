#!/usr/bin/env bash 

cd voter-records
printf "https://voterrecords.com/voters/glastonbury-ct/%s\\n" {1..2653} | xargs -n 1 -P 10 wget -q
