#!/bin/bash

var = 0

declare -a LOSS=(0.59241 0.56645 0.61412 0.60967 0.64170 0.66199 0.67009 0.67881 0.62301 0.67559 0.60530 0.55948)

for i in ./logdir/train/2016-10-26T15-26-03/model.ckpt-85018 ./logdir/train/2016-10-26T15-26-03/model.ckpt-85020 ./logdir/train/2016-10-26T15-26-03/model.ckpt-85100 ./logdir/train/2016-10-26T15-26-03/model.ckpt-85440 ./logdir/train/2016-10-26T15-26-03/model.ckpt-85441 ./logdir/train/2016-10-26T15-26-03/model.ckpt-85660 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86114 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86149 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86245 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86246 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86248 ./logdir/train/2016-10-26T15-26-03/model.ckpt-86255



do
	for word in $i
	do
		#python generate_TYPE.py  --samples=1000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json $word
		echo $word
		echo ${LOSS[$var]}

		#python generate_TYPE.py  --samples=1000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json --loss=${LOSS[$var]}  $word

		var=$((var+1))

	done
done


