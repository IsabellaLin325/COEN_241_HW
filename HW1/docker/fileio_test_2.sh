#!/bin/bash

dir=d_fileio_test_out2.txt
if [ ! -f $dir ]
then
	touch $dir
fi

echo "Test 2 ========> num of threads 16, total file size 3G" >> $dir

for((i=1;i<6;i++))
do
	echo "$i iteration" >> $dir
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=3G --file-test-mode=rndrw --max-time=30 prepare
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=3G --file-test-mode=rndrw --max-time=30 run >> $dir
	sysbench --test=fileio --num-threads=16 --max-requests=0 --file-total-size=3G --file-test-mode=rndrw --max-time=30 cleanup
done
