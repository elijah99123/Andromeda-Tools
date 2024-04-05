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

count=1
for i in atoms:
 for j in np.arange(0,6):
  k= ((i-1)*6)+j+1
  os.system('mkdir '+'{:04d}'.format(k))
  os.system('mv ./vasprun.POSCAR-'+str(k)+'.xml ./'+'{:04d}'.format(k)+'/vasprun.xml')
  count=count+1
