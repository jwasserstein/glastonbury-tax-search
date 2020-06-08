#!/usr/bin/env bash

post_request1='actionType=Name&taxPayerName='
post_request2='&searchbtn=Search&propertyNumber=&propertyName=&billYear=&billType=&billNum=&uniqueId=&linkYear=&linkType=MV&linkNum=&taxId=&recordType=0'

j=()
while read name; do
	j+=($name)
done < <(comm -13 <(ls tax-records) formatted-names.txt)  # find all items that need to be downloaded (in foratted-names.txt), but haven't been downloaded already (in ls tax-records)

cd tax-records
wget -q --keep-session-cookies --save-cookies cookies.txt --delete-after "https://www.mytaxbill.org/inet/bill/home.do?town=glastonbury"
echo -e ${j[@]} | xargs -n 1 -I{} -P 10 wget -q -O "{}" --load-cookies cookies.txt --post-data "$post_request1{}$post_request2" https://www.mytaxbill.org/inet/bill/search.do
rm cookies.txt
