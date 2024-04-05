#!/usr/bin/env bash 

for file in /gsfs0/data/beginel/Documents/111g-D3BJ/vibration/*/*/Needed/Completed/*/
do
 if [ ! -e OUTCAR ]; then
  if [ -e good_sub.py ]; then
   echo $file >> Curr_count.out
  fi
 fi
done

echo "All_done" >> Curr_count.out