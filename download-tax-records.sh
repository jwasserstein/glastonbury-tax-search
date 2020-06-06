#!/usr/bin/env bash

post_request1='actionType=Name&taxPayerName='
post_request2='&searchbtn=Search&propertyNumber=&propertyName=&billYear=&billType=&billNum=&uniqueId=&linkYear=&linkType=MV&linkNum=&taxId=&recordType=0'

j=()
while read name; do
	j+=($name)
done < formatted-names.txt

cd tax-records
wget -q --keep-session-cookies --save-cookies cookies.txt --delete-after "https://www.mytaxbill.org/inet/bill/home.do?town=glastonbury"
echo -e ${j[@]:1:30} | xargs -n 1 -I{} -P 10 wget -q -O "{}" --load-cookies cookies.txt --post-data "$post_request1{}$post_request2" https://www.mytaxbill.org/inet/bill/search.do
rm cookies.txt
