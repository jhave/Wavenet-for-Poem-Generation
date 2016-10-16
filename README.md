
# A TensorFlow implementation of DeepMind's WaveNet paper for POEM generation.

Based almost entirely on Samuel Graván's  (Zeta36) tensorflow-tex-wavenet <b>https://github.com/Zeta36/tensorflow-tex-wavenet</b>. Modified to allow for line breaks, and more flexible saving of models so that it is possible to capture fluctuations in the parameters. 

Blog post describing process and resultant poems: 
http://bdp.glia.ca/wavenet-for-poem-generation-preliminary-results

# Based on Samuel Graván's(Zeta36) tensorflow-tex-wavenet 
# A TensorFlow implementation of DeepMind's WaveNet paper for text generation.


## Requirements

TensorFlow needs to be installed before running the training script.
TensorFlow 0.10 and the current `master` version are supported.

## Training the network

You can use any text (`.txt`) file.

In order to train the network, execute
```bash
python train.py --data_dir=data
```
to train the network, where `data` is a directory containing `.txt` files.
The script will recursively collect all `.txt` files in the directory.

You can see documentation on each of the training settings by running
```bash
python train.py --help
```

You can find the configuration of the model parameters in [`wavenet_params.json`](./wavenet_params.json).
These need to stay the same between training and generation.

## Generating text

You can use the `generate.py` script to generate audio using a previously trained model.

Run
```
python generate.py --samples 16000 model.ckpt-1000
```
where `model.ckpt-1000` needs to be a previously saved model.
You can find these in the `logdir`.
The `--samples` parameter specifies how many characters samples you would like to generate.

The generated waveform can be stored as a
`.txt` file by using the `--text_out_path` parameter:
```
python generate.py --text_out_path=mytext.txt --samples 1500 model.ckpt-1000
```

Passing `--save_every` in addition to `--text_out_path` will save the in-progress wav file every n samples.
```
python generate.py --text_out_path=mytext.txt --save_every 2000 --samples 1500 model.ckpt-1000
```

Fast generation is enabled by default.
It uses the implementation from the [Fast Wavenet](https://github.com/tomlepaine/fast-wavenet) repository.
You can follow the link for an explanation of how it works.
This reduces the time needed to generate samples to a few minutes.

To disable fast generation:
```
python generate.py --samples 1500 model.ckpt-1000 --fast_generation=false
```
