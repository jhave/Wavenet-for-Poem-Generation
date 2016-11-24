#!/bin/bash

printf "\n\n256dilations_2048skipChannels\n\n*******************\n\n"

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/256dilations_2048skipChannels/model.ckpt-27148

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/256dilations_2048skipChannels/model.ckpt-33800

printf "\n\n1024dilations_1024skipChannels\n\n*******************\n\n"

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels1024.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/1024dilations_1024skipChannels/model.ckpt-62324

printf "\n\ndilations1024_skipChannels4096_qc1024_dc32\n\n*******************\n\n"

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-49523

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50601

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-50603

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58102

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-58111

python generate_TYPE.py  --samples=600 --wavenet_params=wavenet_params_ORIG_dilations1024_skipChannels4096_qc1024_dc32.json /Users/jhave/Desktop/github/Wavenet-for-Poem-Generation/logdir/train/demos/dilations1024_skipChannels4096_qc1024_dc32/model.ckpt-59252
