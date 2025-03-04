#!/usr/bin/env bash

cd street-records

a=$(seq 65 90)  # generate an array of numbers 65 - 90 that represent A-Z
for i in $a; do
	printf "gis.vgsi.com/glastonburyct/Streets.aspx?Letter=\\$(printf %o $i)" | xargs wget  # convert code points to character
	sleep 5
done
