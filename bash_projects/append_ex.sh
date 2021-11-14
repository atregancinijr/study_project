#!/bin/bash

size="10"
list=()
for ((ii=0; ii<$size; ii++))
do
	list+=$ii
done
for i in "${list[@]}"; do printf "%s\n" $i >> appended_txt.txt; done
