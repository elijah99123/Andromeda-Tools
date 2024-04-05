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
parser.add_argument("end_file", help="End image file; POSCAR or QE format")
args = parser.parse_args()

atoms1 = io.read(args.start_file)
atoms2 = io.read(args.end_file)

constrain = atoms1.constraints

atom_type = atoms1.numbers
pos1 = atoms1.get_positions()
pos2 = atoms2.get_positions()

a = np.linalg.norm(atoms2.get_cell()[0])
b = np.linalg.norm(atoms2.get_cell()[1])
c = np.linalg.norm(atoms2.get_cell()[2])

v1 = atoms2.get_cell()[0]/a
v2 = atoms2.get_cell()[1]/b
v3 = atoms2.get_cell()[2]/c

a1=atoms2.get_cell_lengths_and_angles()[3]
a2=atoms2.get_cell_lengths_and_angles()[4]
a3=atoms2.get_cell_lengths_and_angles()[5]

a1=np.radians(a1)
a2=np.radians(a2)
a3=np.radians(a3)

omega=np.dot(a*v1,np.cross(b*v2,c*v3))
conversion = np.zeros([3,3])
conversion[0,0] = 1/a
conversion[0,1] = -np.cos(a3)/(a*np.sin(a3))
conversion[0,2] = b*c*(np.cos(a1)*np.cos(a3)-np.cos(a2))/(omega*np.sin(a3))
conversion[1,1] = 1/(b*np.sin(a3))
conversion[1,2] = a*c*(np.cos(a2)*np.cos(a3)-np.cos(a1))/(omega*np.sin(a3))
conversion[2,2] = a*b*np.sin(a3)/omega

for i in np.arange(0,atom_type.size):
 pos1[i] = np.dot(conversion,pos1[i])
 pos2[i] = np.dot(conversion,pos2[i])

count = []

start = atom_type[0]
i = 0
while(start==atom_type[i]):
 i=i+1

count.append(i)
last=i
start=atom_type[i]
while(start==atom_type[i]):
 i=i+1
count.append(i-last)

last=i
start=atom_type[i]
while(start==atom_type[i]):
 i=i+1
count.append(i-last)

last=i
start=atom_type[i]
while(start==atom_type[i]):
 i=i+1
count.append(i-last)

count.append(atom_type.size-i)

#done finding count

new_pos=np.zeros([atom_type.size,3])


found = np.zeros([atom_type.size])
dist_list = np.zeros([atom_type.size])

added = np.arange(0,count[0])
for i in np.arange(0,count[0]):
 curr_min=100000
 for j in added:
  x = min( abs(pos1[i,0]-pos2[j,0]), abs(pos1[i,0]-pos2[j,0]+1), abs(pos1[i,0]-pos2[j,0]-1))
  y = min( abs(pos1[i,1]-pos2[j,1]), abs(pos1[i,1]-pos2[j,1]+1), abs(pos1[i,1]-pos2[j,1]-1))
  z = min( abs(pos1[i,2]-pos2[j,2]), abs(pos1[i,2]-pos2[j,2]+1), abs(pos1[i,2]-pos2[j,2]-1))
  dist = (x)**2 +(y)**2 +(z)**2
  if(dist<curr_min):
   found[i] = j
   curr_min=dist
   dist_list[i]=dist
   #print(str(i) + ";  " +str(j) + ";  " +str(dist))
 added = np.delete(added,np.where(added==found[i]))

added = np.arange(count[0],count[0]+count[1])
for i in np.arange(count[0],count[0]+count[1]):
 curr_min=100000
 for j in added:
  x = min( abs(pos1[i,0]-pos2[j,0]), abs(pos1[i,0]-pos2[j,0]+1), abs(pos1[i,0]-pos2[j,0]-1))
  y = min( abs(pos1[i,1]-pos2[j,1]), abs(pos1[i,1]-pos2[j,1]+1), abs(pos1[i,1]-pos2[j,1]-1))
  z = min( abs(pos1[i,2]-pos2[j,2]), abs(pos1[i,2]-pos2[j,2]+1), abs(pos1[i,2]-pos2[j,2]-1))
  dist = (x)**2 +(y)**2 +(z)**2
  if(dist<curr_min):
   found[i] = j
   curr_min=dist
   dist_list[i]=dist
   #print(str(i) + ";  " +str(j) + ";  " +str(dist))
 added = np.delete(added,np.where(added==found[i]))

added = np.arange(count[0]+count[1],atom_type.size)
for i in np.arange(count[0]+count[1],atom_type.size):
 curr_min=100000
 for j in added:
  x = min( abs(pos1[i,0]-pos2[j,0]), abs(pos1[i,0]-pos2[j,0]+1), abs(pos1[i,0]-pos2[j,0]-1))
  y = min( abs(pos1[i,1]-pos2[j,1]), abs(pos1[i,1]-pos2[j,1]+1), abs(pos1[i,1]-pos2[j,1]-1))
  z = min( abs(pos1[i,2]-pos2[j,2]), abs(pos1[i,2]-pos2[j,2]+1), abs(pos1[i,2]-pos2[j,2]-1))
  dist = (x)**2 +(y)**2 +(z)**2
  if(dist<curr_min):
   found[i] = j
   curr_min=dist
   dist_list[i]=dist
   #print(str(i) + ";  " +str(j) + ";  " +str(dist))
 added = np.delete(added,np.where(added==found[i]))

for i in np.arange(0,count[0]+count[1]):
 new_pos[i,0]= pos2[int(found[i]),0]
 new_pos[i,1]= pos2[int(found[i]),1]
 new_pos[i,2]= pos2[int(found[i]),2]

for i in np.arange(count[0]+count[1],atom_type.size):
 new_pos[i,0]= pos2[int(found[i]),0]
 new_pos[i,1]= pos2[int(found[i]),1]
 new_pos[i,2]= pos2[int(found[i]),2]

q = Atoms('Pd191Zn1C10O1H20', scaled_positions=new_pos, cell=atoms2.get_cell(), pbc=True)

q.set_constraint(constrain)

#vasp.write_vasp("POSCAR_made", atoms1, sort=False, vasp5=True)
vasp.write_vasp("CONTCAR_made.vasp", q, direct=True, sort=False, vasp5=True)

