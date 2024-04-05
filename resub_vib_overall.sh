#!/usr/bin/env bash 

for file in /gsfs0/data/beginel/Documents/111g-D3BJ/vibration/*/*/Needed/Completed/*/
do
 cd $file
 if [ ! -e OUTCAR ]; then
  if [ -e good_sub.py ]; then
   echo $file
   chmod +x good_sub.py
   ./good_sub.py
   sleep 60
  fi
 fi
done

echo "All_done"