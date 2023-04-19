import os
os.chdir("./dataset_2/train")
for i in range(ord("A"),ord("Z")+1):
    os.mkdir(chr(i))