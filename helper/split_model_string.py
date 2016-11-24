
import pandas as pd
import numpy as np


string="""---
loss_value= 0.543735
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-67779
 Done.

---
loss_value= 0.509763
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-67840
 Done.
step 67841 - loss = 0.587, (21.297 sec/step)

---
loss_value= 0.587265
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-67841
 Done.
step 67842 - loss = 0.610, (21.334 sec/step)

---
loss_value= 0.609844
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-67842
 Done.
step 67843 - loss = 0.748, (21.327 sec/step)
step 67844 - loss = 0.579, (21.594 sec/step)

---
loss_value= 0.579112
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-67844
 Done."""


info = {}
content = []

model_str=string.split("/model.ckpt-")
model_str.pop(0)

loss_str=string.split("loss_value= ") 
loss_str.pop(0)

for idx,val in enumerate(model_str):
	info["Model"]= val[:50]
	info["Loss"]= loss_str[idx][:6]
	content.append(info)


print(content)



# ml = []
# for idx,val in enumerate(model_str):
# 	ml.append(val[:5])

# for idx,val in enumerate(loss_str):
# 	ml.append(val[:6])

# print (ml)
