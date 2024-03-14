import os
import paths_files as pf

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

run_check = [0]*100
sim = 0
nao = 0

for i in range(1,101):
    if newest(pf.path_t0+str(i)) == pf.path_t0+str(i)+'/'+pf.ParEst_t0:
        run_check[i-1] = 'SIM\n' #RODOU
        sim += 1
    else:
        run_check[i-1] = 'NAO\n' #NAO RODOU
        nao += 1

with open('run_check_'+pf.dir_t0, 'w') as file:
    file.writelines(run_check)

print('Rodaram: '+str(sim))
print('Nao rodaram: '+str(nao))





