#!/usr/bin/env bash 

for file in ../*
do
  if [ ! -d "$file" ]; then
      name="$(basename $file)" 
      echo $name
      mkdir ./$name
      cp $file ./$name/POSCAR
      cp ./INCAR ./$name/INCAR
      cp ./POTCAR ./$name/POTCAR
      cp ./KPOINTS ./$name/KPOINTS
      cp ./good_sub.py ./$name/good_sub.py
  fi
done
