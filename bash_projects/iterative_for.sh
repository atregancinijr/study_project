#!/bin/bash

size="10"
rm dados.txt
for ((c=0; c<size; c++)) 
do
	echo "$c" >> dados.txt 
done
