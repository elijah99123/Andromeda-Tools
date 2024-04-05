#!/usr/bin/env bash 

for d in ./*/ ; do
    name="$(basename $d)" 
    python3 ./remove_forces.py ./$name/vasprun.xml ./$name/new_vasprun.xml ./hessian_atoms.ndx

done

