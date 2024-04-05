#starts at zero so -1 to all atoms
from xml.etree import ElementTree
import argparse
import numpy as np

atoms=np.arange(192,224)
atoms = np.append(atoms, 36)
atoms = np.append(atoms, 39)
atoms = np.append(atoms, 45)
atoms = np.append(atoms, 18)

atoms = [x - 1 for x in atoms]

parser = argparse.ArgumentParser()
parser.add_argument("read_file", help="Vasp XML file to read")
parser.add_argument("write_file", help="File to write edited XML")

args = parser.parse_args()

def get_indices(ndx_file):
    indices = []
    with open(ndx_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        for i in line.strip().split():
            indices.append(int(i))
    return indices

def remove_v(array, ndx_list):
    ndx_list = set(ndx_list)
    remove_list = []
    for n, child in enumerate(array):
        if n not in ndx_list:
            remove_list.append(child)
    for child in remove_list:
        array.remove(child)

tree = ElementTree.parse(args.read_file)
root = tree.getroot()
force_array = forces = root.findall('.//varray[@name="forces"]')[0]

remove_v(force_array, atoms)

tree.write(args.write_file)

