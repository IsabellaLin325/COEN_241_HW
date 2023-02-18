#!/bin/bash

dir=d_cpu_test_out1.txt
if [ ! -f $dir ]
then
	touch $dir
fi

echo "Test 1 ========> num of threads 4; max prime 20000" >> $dir

for((i=1;i<6;i++))
do
	echo "$i iteration" >> $dir
	sysbench --test=cpu --num-threads=4 --cpu-max-prime=20000 --max-time=30 run >> $dir
done
