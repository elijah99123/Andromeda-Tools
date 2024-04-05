import sys
import os
import subprocess
from math import *
import numpy as np
from ase import io

#os.system('')
#subprocess.getoutput("")

atoms1=io.read("POSCAR")
pos1 = atoms1.get_positions()
atoms2=io.read("MID.vasp")
pos2 = atoms2.get_positions()
atoms3=io.read("CONTCAR")
pos3 = atoms3.get_positions()

for i in range(0,len(pos1)):
 dist1=sqrt((pos1[i,0]-pos2[i,0])**2 + (pos1[i,1]-pos2[i,1])**2 + (pos1[i,2]-pos2[i,2])**2)
 dist2=sqrt((pos1[i,0]-pos3[i,0])**2 + (pos1[i,1]-pos3[i,1])**2 + (pos1[i,2]-pos3[i,2])**2)
 if(dist1>= 0.2):
  print(str(i)+"; "+str(dist1))
 else:
  if(dist2>=0.2):
   print(str(i)+"; "+str(dist2))