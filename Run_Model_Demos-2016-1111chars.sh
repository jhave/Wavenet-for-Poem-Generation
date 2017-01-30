#!/bin/bash

printf "\n\nWavenet for Poem Generation.\nInitializing.\nPlease wait.\n\n"

declare -i samples=1111

# #256dilations_2048skipChannels
# wavenet_params="wavenet_params_ORIG_dilations256_skipChannels2048.json"

# declare -a LOSS=(0 0 )

# for i in ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-27148 ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-33800


# do
# 	for word in $i
# 	do
# 		python generate_Poems_2016.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

# 		var=$((var+1))
# 	done
# done



# ################
# declare -i var=0
# ################


# #1024dilations_1024skipChannels
# wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels1024.json"

# declare -a LOSS=(0 )

# for i in ./logdir/train/demos/1024dilations_1024skipChannels/model.ckpt-62324


# do
# 	for word in $i
# 	do
# 		python generate_Poems_2016.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

# 		var=$((var+1))
# 	done
# done


# ################
# declare -i var=0
# ################


# #  39-18 
# wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc8.json"

# declare -a LOSS=(0.359 0.331 0.342 0.647 0.321 0.501 0.319 0.615 0.32 )

# for i in ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-42013 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-84953 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-93539 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-94028 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-102129 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-110714 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-119305 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-124484 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc8/model.ckpt-127893


# do
# 	for word in $i
# 	do
# 		python generate_Poems_2016.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

# 		var=$((var+1))
# 	done
# done


# ################
# declare -i var=0
# ################


# # 38-59 
# wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc16.json"

# declare -a LOSS=(0.306 0.327 0.33 )

# for i in ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc16/model.ckpt-84953 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc16/model.ckpt-102130 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc16/model.ckpt-119303


# do
# 	for word in $i
# 	do
# 		python generate_Poems_2016.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

# 		var=$((var+1))
# 	done
# done


################
declare -i var=0
################


# 26-03 
wavenet_params="wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json"

declare -a LOSS=(0.497 0.303 0.524 0.521 0.504 0.536 0.284 0.293 0.303 0.278 0.288 0.293 0.280 0.607 0.549 0.625 0.506)

for i in ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-49523 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50601 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50603 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58102 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58111 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-59252 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-67777 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-67778 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-84951 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-93541 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-93542 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-102127 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-102129 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-102616 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-103431 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-107721 ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-107723


do
	for word in $i
	do
		python generate_Poems_2016.py  --samples=$samples --wavenet_params=$wavenet_params --loss=${LOSS[$var]}  $word

		var=$((var+1))
	done
done




