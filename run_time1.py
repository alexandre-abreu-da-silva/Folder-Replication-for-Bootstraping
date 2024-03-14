import os
import paths_files as pf

for f in  os.listdir(pf.batch_t1):
    command = "qsub  "+pf.batch_t1+"/"+f+pf.runfile_t1
    cmd = os.popen(command)
    print(cmd)