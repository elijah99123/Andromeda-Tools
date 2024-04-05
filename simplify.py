import os
import numpy as np

from ase import io
from ase import Atoms
from ase.geometry import Cell
from ase.io import vasp
from scipy.spatial.transform import Rotation
import argparse

atoms1 = io.read("POSCAR")
pos1 = atoms1.get_positions()

new_pos=[]
for i in pos1:
 print(i)
 if(i[2]>7):
  new_pos.append(i)

q = Atoms('Pd63Cu1C10O1H20', new_pos, cell=atoms1.get_cell(), pbc=True)
vasp.write_vasp("CONTCAR_made.vasp", q, direct=True, sort=False, vasp5=True)
os.system('mv POSCAR POSCAR_original.vasp')
os.system('mv CONTCAR_made.vasp POSCAR')
os.system('/mmfs1/data/beginel/Documents/Tool/POSCARtoolkit.py -i POSCAR -f')
os.system('rm -f POSCAR')
os.system('mv POSCAR_C POSCAR')