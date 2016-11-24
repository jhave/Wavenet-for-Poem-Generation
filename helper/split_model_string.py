
import pandas as pd
import numpy as np


string="""#!/bin/bash

string ="---
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
 Done.

---
loss_value= 0.550844
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-73369
 Done.
step 73370 - loss = 0.627, (16.828 sec/step)

---
loss_value= 0.62689
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-73370
 Done.
step 73371 - loss = 0.504, (22.365 sec/step)

---
loss_value= 0.503808
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-73371
 Done.

---
loss_value= 0.548532
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-74908
 Done.

---
loss_value= 0.591448
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-74928
 Done.

---
loss_value= 0.597602
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-75092
 Done.

---
loss_value= 0.544779
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-75277
 Done.
step 75278 - loss = 0.530, (22.298 sec/step)

---
loss_value= 0.529545
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-75278
 Done.

---
loss_value= 0.549426
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-75287
 Done.

---
loss_value= 0.567244
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76362
 Done.
step 76363 - loss = 0.306, (16.702 sec/step)

---
loss_value= 0.30606
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76363
 Done.
step 76364 - loss = 0.298, (16.698 sec/step)

---
loss_value= 0.297512
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76364
 Done.
step 76365 - loss = 0.283, (16.635 sec/step)

---
loss_value= 0.282739
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76365
 Done.
step 76366 - loss = 0.296, (21.716 sec/step)

---
loss_value= 0.295622
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76366
 Done.
step 76367 - loss = 0.561, (21.747 sec/step)

---
loss_value= 0.561443
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76367
 Done.

---
loss_value= 0.521486
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76428
 Done.
step 76429 - loss = 0.565, (21.946 sec/step)

---
loss_value= 0.565372
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76429
 Done.
step 76430 - loss = 0.613, (22.013 sec/step)

---
loss_value= 0.613035
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76430
 Done.
step 76431 - loss = 0.734, (22.053 sec/step)
step 76432 - loss = 0.569, (22.081 sec/step)

---
loss_value= 0.5688
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76432
 Done.

---
loss_value= 0.639686
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76512
 Done.

---
loss_value= 0.612455
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76852
 Done.
step 76853 - loss = 0.689, (21.952 sec/step)

---
loss_value= 0.688732
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-76853
 Done.

---
loss_value= 0.603276
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-77660
 Done.

---
loss_value= 0.683941
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-81543
 Done.
step 81544 - loss = 0.570, (16.829 sec/step)

---
loss_value= 0.569982
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-81544
 Done.

---
loss_value= 0.581688
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-81957
 Done.
step 81958 - loss = 0.600, (21.870 sec/step)

---
loss_value= 0.600248
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-81958
 Done.
step 81959 - loss = 0.496, (21.865 sec/step)

---
loss_value= 0.496486
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-81959
 Done.

---
loss_value= 0.54671
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-83496
 Done.

---
loss_value= 0.558995
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-83516
 Done.

---
loss_value= 0.53802
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84950
  Done.
step 84951 - loss = 0.303, (24.716 sec/step)

---
loss_value= 0.303119
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84951
 Done.
step 84952 - loss = 0.309, (24.917 sec/step)

---
loss_value= 0.308595
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84952
 Done.
step 84953 - loss = 0.287, (22.470 sec/step)

---
loss_value= 0.286646
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84953
 Done.
step 84954 - loss = 0.297, (22.764 sec/step)

---
loss_value= 0.297461
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84954
 Done.
step 84955 - loss = 0.598, (22.832 sec/step)

---
loss_value= 0.597695
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-84955
 Done.

---
loss_value= 0.502616
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85016
 Done.
step 85017 - loss = 0.575, (22.872 sec/step)

---
loss_value= 0.57519
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85017
 Done.

---
loss_value= 0.592412
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85018
 Done.

---
loss_value= 0.566451
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-85020
 Done."

 set -f
 array=(${string//Done/})
 for i in "${!array[@]}"
 do
     echo "$i=>{array[i]}"
 done"""


from collections import defaultdict

info = {}
content = []

dir_str=string.split("Storing checkpoint to ")
dir_str.pop(0)

model_str=string.split("/model.ckpt-")
#model_str=string.split("...checkpoint_path= ")
model_str.pop(0)

loss_str=string.split("loss_value= ") 
loss_str.pop(0)

# >>> from collections import defaultdict
# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> for k, v in s:
#         d[k].append(v)

for idx,val in enumerate(model_str):
	content.append(dir_str[idx][:34]+"/"+val[:5])#+" "+loss_str[idx][:6])
	#content.append(val[:50]+"_"+loss_str[idx][:6])



# for idx,val in enumerate(model_str):
# 	info["Model"]= val[:5]
# 	info["Loss"]= loss_str[idx][:6]
# 	print("INFO",info)
# 	content.append(info)
# 	print("CONTENT",content)

print(content)



# ml = []
# for idx,val in enumerate(model_str):
# 	ml.append(val[:5])

# for idx,val in enumerate(loss_str):
# 	ml.append(val[:6])

# print (ml)
