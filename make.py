import os
os.chdir("./dataset_gray_244/train")
for i in range(ord("A"),ord("Z")+1):
    os.mkdir(chr(i))