import os
import paths_files as pf

for f in  os.listdir(pf.batch_t0):
    command = "qsub  "+pf.batch_t0+"/"+f+pf.runfile_t0
    cmd = os.popen(command)
    print(cmd)
