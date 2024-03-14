import shutil
import paths_files as pf
import os

for i in range(1,101):
    shutil.copytree(pf.dir_t0, pf.path_t0+str(i), dirs_exist_ok=True)

###############################################################################
########################   P R I N C I P A L  #################################
###############################################################################

for j in range(1,101):
    with open(pf.path_t0+str(j)+pf.principal_t0,'r',encoding='utf-8') as file:
        code_p= file.read()

    code_p = code_p.replace('$$$',str(j))
    
    with open(pf.path_t0+str(j)+pf.principal_t0, 'w', encoding='utf-8') as file:
        file.write(code_p)
       
###############################################################################
###########################   S I M A N N E A L   #############################
###############################################################################
       
for k in range(1,101):
    with open(pf.path_t0+str(k)+pf.simanneal_t0,'r',encoding='utf-8') as file:
        code_s= file.read()
   
    code_s = code_s.replace('$$$',str(k))
   
    with open(pf.path_t0+str(k)+pf.simanneal_t0, 'w', encoding='utf-8') as file:
        file.write(code_s)

###############################################################################
#############################   R U N F I L E   ###############################
###############################################################################

main_folder = os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1]
#Pega a pasta atual do script
#Se algum dia parar de funcionar substituir por algo como main_folder = eh0_comp0

for l in range(1,101):
    with open(pf.path_t0+str(l)+pf.runfile_t0,'r',encoding='utf-8') as file:
        code_run= file.readlines()
    
    code_run[15] = '#$ -N '+pf.boots_t0+str(l)+'\n'
    code_run[22] = '/share/apps/matlabR2015b/bin/matlab --qsub -nodisplay -r \"run(\'/home/rnarita/'+main_folder+'/'+pf.path_t0+str(l)+pf.simanneal_t0+'\');exit;\" -logfile test'
   

    with open(pf.path_t0+str(l)+pf.runfile_t0, 'w', encoding='utf-8') as file:
        file.writelines(code_run)