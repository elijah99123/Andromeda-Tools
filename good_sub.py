#!/gsfs0/public/anaconda/3-2018.12.P3.7/bin/python3
import sys
import os
import subprocess
from math import *
import numpy as np

#os.system('')
#subprocess.getoutput("")

check=[]
check.append("005")
check.append("006")
check.append("007")
check.append("008")
check.append("009")
check.append("010")
check.append("011")
check.append("012")
check.append("013")
check.append("014")
check.append("015")
check.append("016")
check.append("017")
check.append("018")
check.append("020")
check.append("021")
check.append("022")
check.append("023")
check.append("024")
check.append("025")
check.append("026")
check.append("027")
check.append("028")
check.append("029")
check.append("030")
check.append("031")
check.append("032")
check.append("033")
check.append("034")
check.append("035")
check.append("036")
check.append("037")
check.append("038")
check.append("039")
check.append("040")
check.append("041")
check.append("042")
check.append("043")
check.append("044")
check.append("045")
check.append("046")
check.append("047")
check.append("048")
check.append("049")
check.append("051")
check.append("052")
check.append("053")
check.append("055")
check.append("056")
check.append("057")
check.append("058")
check.append("059")
check.append("060")
check.append("067")
check.append("068")
check.append("070")
check.append("071")
check.append("073")
check.append("074")
check.append("076")
check.append("077")
check.append("079")
check.append("080")
check.append("085")
check.append("086")
check.append("095")
check.append("102")
check.append("103")
check.append("105")
check.append("106")
check.append("108")
check.append("109")
check.append("110")
check.append("112")
check.append("114")
check.append("116")
check.append("118")
#check.append("119") too slow
check.append("120")
check.append("121")
check.append("123")
check.append("131")
check.append("132")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

line = subprocess.getoutput("pbshosts")

a = line.split("\n")

good=[]
for i in a:
 if(i[18:20]=="fr"): #check if available
  if(int(i[32:34])>20):  #check if enough cores
   if(i[7:10] in check): #check if in list of "good cores"
    if(float(i[54:60])>62): #check if enough memory
     good.append(i)

if(len(good)>0):
 node = good[0][0:10]
 print(node)
 file=subprocess.getoutput("pwd")
 ofile = open(file+'/ni.pbs', 'w')
 print("#!/bin/tcsh", file=ofile)
 print("#PBS -l walltime=120:00:00", file=ofile)
 print("#PBS -l nodes="+node+":ppn=20", file=ofile)
 print("#PBS -l mem=60GB", file=ofile)
 print("#PBS -q normal", file=ofile)
 print("echo $HOST", file=ofile)
 print("cd $PBS_O_WORKDIR", file=ofile)
 print("module load /gsfs0/data/baoju/ForGroup/modulefiles/vasp.5.4.4.CINEB", file=ofile)
 print("echo $PBS_JOBID > JOBID.txt", file=ofile)
 print("mpirun -np `wc -l $PBS_NODEFILE | awk '{print $1}'` $VASP_EXEC/vasp_gam", file=ofile)
 ofile.close()
 os.system('qsub ni.pbs')
 
else:
 print("no available nodes")