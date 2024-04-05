#!/usr/public/anaconda/2020.07-p3.8/bin/python3
import sys
import os
import subprocess
from math import *
import numpy as np

atoms=np.arange(192,224)
atoms = np.append(atoms, 36)
atoms = np.append(atoms, 39)
atoms = np.append(atoms, 45)
print(atoms)

os.system('mkdir Needed')

for i in atoms:
 for j in np.arange(0,6):
  k= ((i-1)*6)+j+1
  if(k<100):
   os.system('cp ./POSCAR-0'+str(k)+' ./Needed/POSCAR-0'+str(k))
  else:
   os.system('cp ./POSCAR-'+str(k)+' ./Needed/POSCAR-'+str(k))
