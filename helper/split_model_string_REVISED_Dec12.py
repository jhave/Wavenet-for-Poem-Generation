
import pandas as pd
import numpy as np



string="""


step 124483 - loss = 0.662, (22.174 sec/step)

---
loss_value= 0.662315 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-124483
 Done.
step 124484 - loss = 0.615, (21.922 sec/step)

---
loss_value= 0.615214 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-124484
 Done.
step 124485 - loss = 1.103, (24.225 sec/step)
step 124486 - loss = 1.227, (22.150 sec/step)
step 124487 - loss = 1.301, (24.212 sec/step)

step 129999 - loss = 1.464, (20.614 sec/step)
step 130000 - loss = 1.396, (20.514 sec/step)
Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-130000
 Done.
step 130001 - loss = 1.376, (20.442 sec/step)
step 130002 - loss = 1.420, (20.609 sec/step)

step 134000 - loss = 6.079, (34.272 sec/step)
step 135000 - loss = 2.079, (23.272 sec/step)
Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-135000
 Done.
step 135001 - loss = 1.958, (27.237 sec/step)
step 135002 - loss = 1.863, (23.206 sec/step)
step 135003 - loss = 1.872, (27.398 sec/step)
step 136478 - loss = 0.595, (26.411 sec/step)

---
loss_value= 0.595127 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-136478
 Done.
step 136479 - loss = 0.458, (30.450 sec/step)

---
loss_value= 0.457558 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-136479
 Done.
step 136480 - loss = 0.485, (25.036 sec/step)

---
loss_value= 0.48456 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-136480
 Done.
step 136481 - loss = 0.500, (31.866 sec/step)

---
loss_value= 0.500328 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-136481
 Done.
step 136482 - loss = 0.492, (24.697 sec/step)

---
loss_value= 0.492336 
---

Storing checkpoint to ./logdir/train/2016-10-26T18-39-18 ...checkpoint_path= ./logdir/train/2016-10-26T18-39-18/model.ckpt-136482
 Done.
step 136483 - loss = 1.288, (26.179 sec/step)





---
loss_value= 0.518228 
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-145066
 Done.
step 145067 - loss = 0.452, (24.516 sec/step)

---
loss_value= 0.452141 
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-145067
 Done.
step 145068 - loss = 0.446, (24.357 sec/step)

---
loss_value= 0.445709 
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-145068
 Done.
step 145069 - loss = 0.456, (23.843 sec/step)

---
loss_value= 0.455939 
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-145069
 Done.
step 145070 - loss = 0.468, (23.785 sec/step)

---
loss_value= 0.467641 
---

Storing checkpoint to ./logdir/train/2016-10-26T15-26-03 ...checkpoint_path= ./logdir/train/2016-10-26T15-26-03/model.ckpt-145070
 Done.



"""





loss_str=string.split("loss_value= ") 
loss_str.pop(0)

#only want first one after the loss declaration otherwise the 500 default saves fuck things up
dirs=[]
loss=[]

for s in loss_str:
	dl =s.split("...checkpoint_path= ")
	dirs.append(dl[1].split(" ")[0].strip("\n"))


	l =s.split(" ")
	loss.append(l[0].strip(" "))
	#print ('L[0]',l[0])


print ("LENGTH:", len(dirs),len(loss))
print ("cut and paste below text into RunModels.sh and bash it to generate text\n\n")


print("declare -a LOSS=("+" ".join(loss),")\n\n")
print("for i in "+" ".join(dirs))
