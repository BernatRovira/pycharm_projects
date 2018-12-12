#!/bin/bash

for i in {100..1000..100} # suboptimal loop
do
	for j in {1..30..1}
	do
		./capacity_check.py $i 3
	done
done

for i in {100..1000..100} # optimal loop
do
	for j in {1..30..1}
	do
		./capacity_check.py $i 1
	done
done
