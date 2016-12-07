#!/bin/bash

declare -i samples=111














wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc8.json"

declare -i var=0

declare -a LOSS=(0.662315 0.615214 0.595127 0.457558 0.48456 0.500328 0.492336 )


for i in ./logdir/train/2016-10-26T18-39-18/model.ckpt-124483 ./logdir/train/2016-10-26T18-39-18/model.ckpt-124484 ./logdir/train/2016-10-26T18-39-18/model.ckpt-136478 ./logdir/train/2016-10-26T18-39-18/model.ckpt-136479 ./logdir/train/2016-10-26T18-39-18/model.ckpt-136480 ./logdir/train/2016-10-26T18-39-18/model.ckpt-136481 ./logdir/train/2016-10-26T18-39-18/model.ckpt-136482


do
	for word in $i
		do
			# echo '------------------'
			# echo $word
			# echo ${LOSS[$var]}

			python generate_TYPE.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

			var=$((var+1))
		done
done

