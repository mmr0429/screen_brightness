#!/usr/bin/env python3
import os,sys


#requires xrandr

device_name="eDP-1" #CHANGE TO YOUR DEVICE NAME
cb_file_path="current_brightness" #YOU WILL NEED TO ADD FULL PATH HERE


step=0.1 #WORKS BEST WITH THIS VALUE

def fread(file_name):
    user_file=open(file_name,"r")
    file_content=user_file.read()
    user_file.close()
    return str(file_content)

def fwrite(file_name, towrite):
    user_file=open(file_name,"w")
    user_file.write(towrite)
    user_file.close()


#a - brighter d - darker
mode=sys.argv[1]

cb=float(fread(cb_file_path))


if mode is "a":
    new_b=cb+step
    new_b=round(new_b,2)
    if new_b >= 1:
        fwrite(cb_file_path,"1")
    else:
        fwrite(cb_file_path,str(new_b))

elif mode is "d":
    new_b=cb-step
    new_b=round(new_b,2)
    if new_b < 0.1:
        fwrite(cb_file_path,"0")
    else:
        fwrite(cb_file_path,str(new_b))

else:
    print("WRONG ARGUMENT")

sb=float(fread(cb_file_path))
os.system('xrandr --output {} --brightness {}'.format(device_name,sb))
