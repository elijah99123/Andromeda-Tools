import os
import numpy as np
from ase import io
from ase.io import vasp
from scipy.spatial.transform import Rotation
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("start_file", help="Starting image file; POSCAR or QE format")
parser.add_argument("end_file", help="End image file; POSCAR or QE format")
parser.add_argument("n_images", help="Number of images")
parser.add_argument("align_indices", help="File with atom indices to perform alignment on; START FROM 0")
parser.add_argument("apply_indices", help="File with atom indices to apply rotation/translation to; START FROM 0")
args = parser.parse_args()

def get_indices(ndx_file):
   indices = []
   with open(ndx_file, 'r') as f:
       lines = f.readlines()
   for line in lines:
       for i in line.strip().split():
           indices.append(int(i))
   return indices
       

align_indices = get_indices(args.align_indices)
apply_indices = get_indices(args.apply_indices)
n_images = int(args.n_images) - 1

atoms1 = io.read(args.start_file)
atoms2 = io.read(args.end_file)

pos1 = atoms1.get_positions()[align_indices, :]
pos2 = atoms2.get_positions()[align_indices, :]

cog1 = np.mean(pos1, axis=0)
cog2 = np.mean(pos2, axis=0)
trans_vec = cog2 - cog1

pos1 = pos1 - cog1
pos2 = pos2 - cog2

r, rmsd = Rotation.align_vectors(pos2, pos1)
rot_vec = r.as_rotvec()
angle = np.linalg.norm(rot_vec)
rot_vec = rot_vec/angle

print('Alignment RMSD:', f'{rmsd:.3f}', 'Angstroms')
if rmsd > 10:
   print('WARNING: The alignment RMSD is greater than 10 Angstroms')
   print('Rotated structure is likely not a rigid body')

pos1 = atoms1.get_positions()[apply_indices, :] - cog1
pos2 = atoms2.get_positions()[apply_indices, :] - cog2
pos2 = r.apply(pos2, inverse=True)
pos_diff = pos2 - pos1

new_atoms = [atoms1]
for i in range(1, n_images):
    
    scale = i/n_images
    t = trans_vec*scale
    a = angle*scale
    v = rot_vec*a
    r = Rotation.from_rotvec(v)
    d = pos_diff*scale
    
    a = io.read(args.start_file)
    p = a.get_positions()
    new_pos = p[apply_indices, :] - cog1 + d
    new_pos = r.apply(new_pos) + cog1 + t 
    p[apply_indices, :] = new_pos
    a.set_positions(p)
    new_atoms.append(a)
new_atoms.append(atoms2)

non_apply = []
for i in np.arange(0,223):
 if(i not in apply_indices):
  non_apply.append(int(i))

pos1 = atoms1.get_positions()
pos2 = atoms2.get_positions()
diff = pos2-pos1
print(diff)
print(np.max(np.array(diff)))

remove=[]
for i in non_apply:
 if(abs(diff[i,0])>15 or abs(diff[i,1])>15 or abs(diff[i,2])>15):
   remove.append(i)
print(remove)

for i in reversed(remove):
 del non_apply[i]

my_atoms=[]
for i in np.arange(0,len(new_atoms)-1):
 a=new_atoms[i]
 p = a.get_positions()
 scale = i/n_images
 p[non_apply,:] = p[non_apply,:]+scale*diff[non_apply,:]
 a.set_positions(p)
 my_atoms.append(a)
j=int(len(new_atoms)-1)
a=new_atoms[j]
my_atoms.append(a)

for n, a in enumerate(my_atoms):
    ddir = f'{n:02d}'
    os.system(f'mkdir -p {ddir}')
    vasp.write_vasp(os.path.join(ddir, 'POSCAR'), a, sort=False, vasp5=True)

