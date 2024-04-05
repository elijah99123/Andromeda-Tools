import os
import numpy as np

from ase import io
from ase import Atoms
from ase.geometry import Cell
from ase.io import vasp
from scipy.spatial.transform import Rotation
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("start_file", help="Starting image file; POSCAR or QE format")
parser.add_argument("index_1")
parser.add_argument("index_2")
parser.add_argument("name")
args = parser.parse_args()

atoms1 = io.read(args.start_file)
constrain = atoms1.constraints

ind1 = int(args.index_1)-1
ind2 = int(args.index_2)-1

pos1 = atoms1.get_positions()

loc1 = [pos1[ind1,0],pos1[ind1,1],pos1[ind1,2]]
loc2 = [pos1[ind2,0],pos1[ind2,1],pos1[ind2,2]]

pos1[ind1] = loc2
pos1[ind2] = loc1

q = Atoms('Pd191Cu1C10O1H20', positions=pos1, cell=atoms1.get_cell(), pbc=True)

q.set_constraint(constrain)

vasp.write_vasp(args.name,q, direct=True,sort=False, vasp5=True)


