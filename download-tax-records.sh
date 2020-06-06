#!/usr/bin/env bash

cookie='Cookie: JSESSIONID=0B9465C773575F90A4422B0A911F3804; __utmc=260872849; __utma=260872849.1384174217.1591365043.1591396829.1591475481.6; __utmz=260872849.1591475481.6.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=260872849.3.10.1591475481'

post_request1='actionType=Name&taxPayerName='
post_request2='&searchbtn=Search&propertyNumber=&propertyName=&billYear=&billType=&billNum=&uniqueId=&linkYear=&linkType=MV&linkNum=&taxId=&recordType=0'

j=()
echo "Beginning loading names"
while read name; do
	j+=($name)
done < formatted-names.txt
echo "Finished loading names"

cd tax-records
echo -e ${j[@]:1:3} | xargs -n 1 -I{} -P 10 wget -O "{}" --header "$cookie" --post-data "$post_request1{}$post_request2" https://www.mytaxbill.org/inet/bill/search.do
