#!/bin/bash



for i in './logdir/train/2016-10-26T15-26-03/67779', './logdir/train/2016-10-26T15-26-03/67840', './logdir/train/2016-10-26T15-26-03/67841', './logdir/train/2016-10-26T15-26-03/67842', './logdir/train/2016-10-26T15-26-03/67844', './logdir/train/2016-10-26T15-26-03/73369', './logdir/train/2016-10-26T15-26-03/73370', './logdir/train/2016-10-26T15-26-03/73371', './logdir/train/2016-10-26T15-26-03/74908', './logdir/train/2016-10-26T15-26-03/74928', './logdir/train/2016-10-26T15-26-03/75092', './logdir/train/2016-10-26T15-26-03/75277', './logdir/train/2016-10-26T15-26-03/75278', './logdir/train/2016-10-26T15-26-03/75287', './logdir/train/2016-10-26T15-26-03/76362', './logdir/train/2016-10-26T15-26-03/76363', './logdir/train/2016-10-26T15-26-03/76364', './logdir/train/2016-10-26T15-26-03/76365', './logdir/train/2016-10-26T15-26-03/76366', './logdir/train/2016-10-26T15-26-03/76367', './logdir/train/2016-10-26T15-26-03/76428', './logdir/train/2016-10-26T15-26-03/76429', './logdir/train/2016-10-26T15-26-03/76430', './logdir/train/2016-10-26T15-26-03/76432', './logdir/train/2016-10-26T15-26-03/76512', './logdir/train/2016-10-26T15-26-03/76852', './logdir/train/2016-10-26T15-26-03/76853', './logdir/train/2016-10-26T15-26-03/77660', './logdir/train/2016-10-26T15-26-03/81543', './logdir/train/2016-10-26T15-26-03/81544', './logdir/train/2016-10-26T15-26-03/81957', './logdir/train/2016-10-26T15-26-03/81958', './logdir/train/2016-10-26T15-26-03/81959', './logdir/train/2016-10-26T15-26-03/83496', './logdir/train/2016-10-26T15-26-03/83516', './logdir/train/2016-10-26T15-26-03/84950', './logdir/train/2016-10-26T15-26-03/84951', './logdir/train/2016-10-26T15-26-03/84952', './logdir/train/2016-10-26T15-26-03/84953', './logdir/train/2016-10-26T15-26-03/84954', './logdir/train/2016-10-26T15-26-03/84955', './logdir/train/2016-10-26T15-26-03/85016', './logdir/train/2016-10-26T15-26-03/85017', './logdir/train/2016-10-26T15-26-03/85018', './logdir/train/2016-10-26T15-26-03/85020'
do
	for word in $i
	do
		python generate_TYPE.py  --samples=1000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json $word
	done
done


