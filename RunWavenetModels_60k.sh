#!/bin/bash
printf "\ndilations: 256  \nskip channels: 2048 \n________________________\n"

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-27148

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json ./logdir/train/demos/256dilations_2048skipChannels/model.ckpt-33800

printf "\ndilations: 1024 \nskipChannels: 1024\n________________________\n"

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels1024.json ./logdir/train/demos/1024dilations_1024skipChannels/model.ckpt-62324

printf "\ndilations: 1024 \nskipChannels: 4096 \nquantization channels: 1024 \ndilaton channels32\n________________________\n"

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-49523

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50601

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50603

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58102

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58111

python generate_TYPE.py  --samples=6000 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json ./logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-59252
