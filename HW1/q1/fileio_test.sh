#!/bin/bash

dir=q1_fileio_test_out1.txt
if [ ! -f $dir ]
then
	touch $dir
fi

echo "Test 1 ========> num of threads 16, total file size 2G" >> $dir

for((i=1;i<6;i++))
do
	echo "$i iteration" >> $dir
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=2G --file-test-mode=rndrw --max-time=30 prepare
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=2G --file-test-mode=rndrw --max-time=30 run >> $dir
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=2G --file-test-mode=rndrw --max-time=30 cleanup
done
