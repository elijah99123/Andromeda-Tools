import os
import numpy as np
import ase
import ase.io as io
from ase.io import read, write
from ase.build import make_supercell
from itertools import combinations

def calculate_bond_lengths(atoms):
    """Calculate bond lengths for all pairs of atoms."""
    bond_lengths = []
    for i, j in combinations(range(len(atoms)), 2):
        distance = np.linalg.norm(atoms.positions[i] - atoms.positions[j])
        bond_lengths.append((i, j, distance))
    return bond_lengths

def increase_bond_lengths(atoms, min_length=1.1):
    """Increase bond lengths to at least min_length."""
    bond_lengths = calculate_bond_lengths(atoms)
    for i, j, distance in bond_lengths:
        if distance < min_length:
            displacement = min_length - distance
            direction = (atoms.positions[j] - atoms.positions[i]) / distance
            atoms.positions[i] -= 0.5 * displacement * direction
            atoms.positions[j] += 0.5 * displacement * direction

for i in np.arange(1,6):
	str_POS = "./0"+str(i)+"/POSCAR"
	POS = io.read(str_POS)
	increase_bond_lengths(POS, min_length=1.1)
	os.system("mv " +str_POS +" ./0"+str(i)+"/POSCAR_old")
	write(str_POS, POS, format='vasp')
