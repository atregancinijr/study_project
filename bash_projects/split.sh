#!/bin/bash
#Example:
greeting() {
	local string="Hello $1"
	echo "$string"
}

split_string(){
	local string="$1"
	local position=$3
	IFS=$2
	read -ra val <<< "$string"
	IFS=' '
	echo ${val[$position]}
}
result2=$(split_string "0xff : 0x123" " : " 1)
echo $result2
