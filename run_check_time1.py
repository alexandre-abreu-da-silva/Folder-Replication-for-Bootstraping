import os
import paths_files as pf


def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

with open('run_check_'+pf.dir_t0,'r') as file:
    run_check_time0 = file.readlines()
    run_check_time0 = [s.strip() for s in run_check_time0]


run_check_time1 = ['blank\n']*100
sim = 0
nao = 0

for i in range(1,101):
    if run_check_time0[i-1] == 'SIM':
        if newest(pf.path_t1+str(i)) == pf.path_t1+str(i)+'/'+pf.ParEst_t1:
            run_check_time1[i-1] = 'SIM\n' #RODOU
            sim += 1
        else:
            run_check_time1[i-1] = 'NAO\n' #NAO RODOU
            nao += 1



with open('run_check_'+pf.dir_t1, 'w') as file:
    file.writelines(run_check_time1)

print('Rodaram: '+str(sim))
print('Nao rodaram: '+str(nao))





