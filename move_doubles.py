#!/usr/public/anaconda/2020.07-p3.8/bin/python3
import sys
import os
import subprocess
from math import *
import numpy as np
from ase.io.vasp import read_vasp, write_vasp

fold1="/gsfs0/data/beginel/Documents/111g-D3BJ/vibration/cis4-done/start/Needed/Completed" #has OUTCAR
fold2="/gsfs0/data/beginel/Documents/111g-D3BJ/vibration/cis3/end/Needed/Completed"  #needs OUTCAR

dir1=os.listdir(fold1)
dir2=os.listdir(fold2)

for i in dir1:
 for j in dir2:
  if(i[0]=="P" and i[2]=="S"):
   if(j[0]=="P" and j[2]=="S"):
    path1=str(fold1)+"/"+str(i)+"/POSCAR"
    path2=str(fold2)+"/"+str(j)+"/POSCAR"
    file1 = open(path1,"r")
    cont1 = file1.read()
    file1.close()
    file2 = open(path2,"r")
    cont2 = file2.read()
    file2.close()
    lines1 = cont1.split("\n")
    lines1.sort()
    lines2 = cont2.split("\n")
    lines2.sort()
    if(lines1==lines2):
     os.system('cp '+str(fold1)+"/"+str(i)+"/OUTCAR"+" "+str(fold2)+"/"+str(j)+"/OUTCAR")
exit()
