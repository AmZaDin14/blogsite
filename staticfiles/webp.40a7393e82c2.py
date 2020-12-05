#!/usr/bin/python3
import glob
import os

quality = str(80)
imgs = glob.glob("img/*")
for img in imgs:
    print(img)

    cmd = ("cwebp -q " + quality + " " + img + " -o " + img[:img.index(".")] + ".webp")

    print(cmd)
    os.system(cmd)
