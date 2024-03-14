import shutil
import os
import numpy as np
import scipy.io as sio
import paths_files as pf

with open('run_check_'+pf.dir_t0,'r',encoding='utf-8') as file:
    run_check_time0 = file.readlines()
    run_check_time0 = [s.strip() for s in run_check_time0]

with open('run_check_'+pf.dir_t1,'r',encoding='utf-8') as file:
    run_check_time1 = file.readlines()
    run_check_time1 = [s.strip() for s in run_check_time1]

path = './Resultados_bootstrap'

try:
    os.mkdir(path)
    print("Folder %s created!" % path)
except FileExistsError:
    print("Folder %s already exists" % path)


for i in range(1,101):
    if run_check_time0[i-1] == 'SIM':
        shutil.copy2(pf.path_t0+str(i)+'/'+pf.ParEst_t0, path+'/'+pf.ParEst_t0.split(sep = '.')[0]+'_boot'+str(i)+'.mat')
        if run_check_time1[i-1] == 'SIM':    
            shutil.copy2(pf.path_t1+str(i)+'/'+pf.ParEst_t1, path+'/'+pf.ParEst_t1.split(sep = '.')[0]+'_boot'+str(i)+'.mat')

    
###############################################################################    
##junta todos os resultados em um arquivo .mat unico (ParEst_eh0_time0_Mex_nokids_allboots.mat e ParEst_eh0_time1_Mex_nokids_allboots.mat)

size_t0 = np.shape(list(sio.loadmat(pf.dir_t0+'/'+pf.ParEst_t0).values())[-1])[1] ## tamanho do vetor solucões de t0
size_t1 = np.shape(list(sio.loadmat(pf.dir_t1+'/'+pf.ParEst_t1).values())[-1])[1]

matrix_t0 = np.zeros((100,size_t0))
matrix_t1 = np.zeros((100,size_t1))

for j in range(1,101):
    if run_check_time0[j-1] == 'SIM':
        x_t0 = sio.loadmat(path+'/'+pf.ParEst_t0.split(sep = '.')[0]+'_boot'+str(j)) #.split para tirar o .mat de ParEst
        x_t0 = list(x_t0.values())[-1]
        matrix_t0[j-1] = x_t0
        if run_check_time1[j-1] == 'SIM':
            x_t1 = sio.loadmat(path+'/'+pf.ParEst_t1.split(sep = '.')[0]+'_boot'+str(j))
            x_t1 = list(x_t1.values())[-1]
            matrix_t1[j-1] = x_t1
 
##As linhas referentes a pastas que nao rodaram ficam com 0
##O codigo a seguir remove as linhas com 0

matrix_t0 = np.delete(matrix_t0, np.where(matrix_t0 == np.zeros(size_t0))[0], axis = 0)
matrix_t1 = np.delete(matrix_t1, np.where(matrix_t1 == np.zeros(size_t1))[0], axis = 0)    

###
## Adicionar coluna indicando qual o numero da pasta referente a cada resultado:


boot_num_t0 = np.zeros((100,1))
boot_num_t1 = np.zeros((100,1))

for k in range(1,101):
    if run_check_time0[k-1] == 'SIM':
        boot_num_t0[k-1] = k
    if run_check_time1[k-1] == 'SIM':
        boot_num_t1[k-1] = k

boot_num_t0 = np.delete(boot_num_t0, np.where(boot_num_t0 == 0)[0], axis = 0) ##deletando os zeros 
boot_num_t1 = np.delete(boot_num_t1, np.where(boot_num_t1 == 0)[0], axis = 0)

matrix_t0 = np.hstack((matrix_t0, boot_num_t0))
matrix_t1 = np.hstack((matrix_t1, boot_num_t1))


###############################################################################
 
mdic_t0 = {'__header__': b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Sat Aug 12 00:23:53 2023',
 '__version__': '1.0',
 '__globals__': [],
 pf.ParEst_t0.split(sep = '.')[0]+'_allboots': matrix_t0}
    
mdic_t1 = {'__header__': b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Wed Aug 16 13:21:28 2023',
 '__version__': '1.0',
 '__globals__': [],
 pf.ParEst_t1.split(sep = '.')[0]+'_allboots': matrix_t1}

sio.savemat(pf.ParEst_t0.split(sep = '.')[0]+'_allboots.mat', mdic_t0)
sio.savemat(pf.ParEst_t1.split(sep = '.')[0]+'_allboots.mat', mdic_t1)