#!/usr/bin/env bash 

for d in ../*/ ; do
    name="$(basename $d)" 
    cp ../$name/vasprun.xml ./vasprun.$name.xml

done

