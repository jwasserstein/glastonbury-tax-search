#!/usr/bin/env bash

cat names.txt | awk '{if($3==""){print $2"+"$1}else{print $3"+"$1}}' | sort | uniq | sed -E "s/'//"
