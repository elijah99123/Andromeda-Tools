#!/usr/bin/env bash 

export comp=/gsfs0/data/beginel/Documents/111g-D3BJ/vibration/cis4/start/Needed/Completed

for file in "/gsfs0/data/beginel/Documents/111g-D3BJ/vibration/cis4/start/Needed"/*
do
  if [ ! -d "$file" ]; then
      name="$(basename $file)" 
      echo $name

      mkdir $comp/$name
      cp $file $comp/$name/POSCAR
      cp $comp/ni.pbs $comp/$name/ni.pbs
      cp $comp/INCAR $comp/$name/INCAR
      cp $comp/POTCAR $comp/$name/POTCAR
      cp $comp/KPOINTS $comp/$name/KPOINTS
      
      cd $comp/$name
      qsub ni.pbs


  fi
done
