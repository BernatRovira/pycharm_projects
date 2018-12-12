#!/bin/bash

for i in {100..1000..100} # suboptimal loop
do
	for j in {1..30..1}
	do
		./fixed_capacity.py $i 0.03 0.03
	done
done
