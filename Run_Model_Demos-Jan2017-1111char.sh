#!/bin/bash

declare -i samples=1111

#256dilations_2048skipChannels
wavenet_params="wavenet_params_ORIG_dilations256_skipChannels2048.json"

declare -a LOSS=(0 0 )

for i in ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-27148 ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-33800


do
	for word in $i
	do
		python generate_TYPE-LaptopMTL.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

		var=$((var+1))
	done
done



################
declare -i var=0
################


#1024dilations_1024skipChannels
wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels1024.json"

declare -a LOSS=(0 )

for i in ./logdir/train/demos/1024dilations_1024skipChannels/model.ckpt-62324


do
	for word in $i
	do
		python generate_TYPE-LaptopMTL.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

		var=$((var+1))
	done
done




################
declare -i var=0
################


#1024dilations_1024skipChannels
wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json"

declare -a LOSS=(0 0 0 0 0 0 0 0 )

for i in ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-59252 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58111 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58102 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50603 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50601 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-49523


do
	for word in $i
	do
		python generate_TYPE-LaptopMTL.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

		var=$((var+1))
	done
done



