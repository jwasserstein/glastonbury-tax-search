#!/usr/bin/env bash 

cd voter-records
seq 1 2653 | xargs -I {} -n 1 -P 10 wget https://voterrecords.com/voters/glastonbury-ct/{}
seq 1 497 | xargs -I {} -n 1 -P 10 wget https://voterrecords.com/voters/south+glastonbury-ct/{}
