#!/bin/bash

dir=d_cpu_test_out2.txt
if [ ! -f $dir ]
then
	touch $dir
fi

echo "Test 2 ========> num of threads 4; max prime 30000" >> $dir

for((i=1;i<6;i++))
do
	echo "$i iteration" >> $dir
	sysbench --test=cpu --num-threads=4 --cpu-max-prime=30000 --max-time=30 run >> $dir
done
