
import pandas as pd
import numpy as np


string="""---
loss_value= 0.592412
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85018
 Done.

---
loss_value= 0.566451
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85020
 Done.

---
loss_value= 0.614123
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85100
 Done.

---
loss_value= 0.609679
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85440
 Done.
step 85441 - loss = 0.642, (22.412 sec/step)

---
loss_value= 0.641703
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85441
 Done.

---
loss_value= 0.661999
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85660
 Done.

---
loss_value= 0.670093
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86114
 Done.

---
loss_value= 0.678813
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86149
 Done.

---
loss_value= 0.623011
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86245
 Done.
step 86246 - loss = 0.676, (22.357 sec/step)

---
loss_value= 0.675596
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86246
 Done.
step 86247 - loss = 0.728, (22.471 sec/step)
step 86248 - loss = 0.605, (22.738 sec/step)

---
loss_value= 0.605301
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86248
 Done.
step 86249 - loss = 1.145, (22.702 sec/step)
step 86250 - loss = 1.017, (22.763 sec/step)
step 86251 - loss = 0.940, (22.346 sec/step)
step 86252 - loss = 0.946, (22.302 sec/step)
step 86253 - loss = 0.785, (22.186 sec/step)
step 86254 - loss = 0.731, (22.528 sec/step)
step 86255 - loss = 0.559, (24.670 sec/step)

---
loss_value= 0.55948
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-86255
 Done."""


from collections import defaultdict

info = {}
model_dict = []
loss_dict = []

dir_str=string.split("...checkpoint_path= ")
dir_str.pop(0)

loss_str=string.split("loss_value= ") 
loss_str.pop(0)


for idx,val in enumerate(dir_str):
	model_dict.append(dir_str[idx][:51])#+"/"+val[:5])#+" "+loss_str[idx][:6])

for idx,val in enumerate(loss_str):
	loss_dict.append(val[:7])


print("MODElS: "," ".join(model_dict))
print("LOSS: "," ".join(loss_dict))
