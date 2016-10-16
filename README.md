
# A TensorFlow implementation of DeepMind's WaveNet paper for POEM generation.


Blog post describing process and resultant poems: <br>
http://bdp.glia.ca/wavenet-for-poem-generation-preliminary-results

Based almost entirely on Samuel Graván's  (Zeta36) tensorflow-tex-wavenet <b>https://github.com/Zeta36/tensorflow-tex-wavenet</b>. 

Modified to allow for line breaks, identifiable generated txt files, and more flexible saving of models so that it is possible to capture fluctuations in the parameters. 


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
This repo includes a txt source with 11k poems in `data/pf`
The script will recursively collect all `.txt` files in the directory.

You can see documentation on each of the training settings by running
```bash
python train.py --help
```

You can find the configuration of the model parameters in [`wavenet_params.json`](./wavenet_params.json).
These need to stay the same between training and generation.

Here's an example training call that keeps all models with loss below 1.0:
```bash
python train_Oct13_Low1_keepALL.py --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json  --data_dir=data/pf
```

If training fails at some point, or you simply want to restart add the following parameter (2016-10-15T20-25-20 is in this example the directory where the models are stored)
```bash
 --restore_from=./logdir/train/2016-10-15T20-25-20/
```

## Generating text

You can use the `generate.py` script to generate poetry using a previously trained model.

Run
```
python generate.py --samples 16000 model.ckpt-1000
```
where `model.ckpt-1000` needs to be a previously saved model.
You can find these in the `logdir`.
The `--samples` parameter specifies how many characters samples you would like to generate.

The generated POETRY is by default saved as a `.txt` file to the GENERATED folder with with DateTime stamp and Model Number ... the following example will be saved to "GENERATED/2016-10-15T20-46-39_Model_15691.txt"
```
python generate_Oct13.py --samples 6000 --wavenet_params=wavenet_params_ORIG_dilations256_skipChannels2048.json ./logdir/train/2016-10-15T20-46-39/model.ckpt-15691
```

Passing `--save_every` will save the file every n samples. I  have used this to create a typewriter like effect where line after line appears in rapid succession. Has potential for performance.
```
python generate.py --save_every 100 --samples 1500 model.ckpt-1000
```

Fast generation is enabled by default.
It uses the implementation from the [Fast Wavenet](https://github.com/tomlepaine/fast-wavenet) repository.
You can follow the link for an explanation of how it works.
This reduces the time needed to generate samples to a few minutes.

To disable fast generation:
```
python generate.py --samples 1500 model.ckpt-1000 --fast_generation=false
```
(Note: As of Oct 16th, I have never disabled fast generation.)
