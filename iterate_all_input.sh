#!/bin/bash

# iterate all raw input
# output to rank.csv filee
for file in ` ls $1 `; do
	python3 html_data_parser.py --file_name $file >> rank.csv
done
