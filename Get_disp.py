#!/usr/public/anaconda/2020.07-p3.8/bin/python3
import sys
import os
import subprocess
from math import *
import numpy as np
from ase.io.vasp import read_vasp, write_vasp

atoms=np.arange(192,224)
atoms = np.append(atoms, 36)
atoms = np.append(atoms, 39)
atoms = np.append(atoms, 45)
atoms = np.append(atoms, 18)
print(atoms)

atoms2=[]
for i in atoms:
 atoms2.append(i-1)

facts = read_vasp("POSCAR")

del_list=[]
for i in np.arange(0,223):
 if(i in atoms2):
  print("nope")
 else:
  del_list.append(i)

del facts[del_list]

write_vasp("CONTCAR",
               facts,
               label=None,
               direct=False,
               sort=False,
               symbol_count=None,
               long_format=True,
               vasp5=True,
               ignore_constraints=False,
               wrap=False)