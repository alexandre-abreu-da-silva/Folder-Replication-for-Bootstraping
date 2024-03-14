# -*- coding: utf-8 -*-
###############################################################################
############ COLOCAR AQUI AS PASTAS E ARQUIVOS: ###############################
###############################################################################
##  Colocar entre aspas (' ou ")
##  Somente o nome do arquivo é necessário, não o caminho completo
##  Não esquecer a extensão do arquivo
###############################time0###########################################
## Pasta time0 a ser replicada:
dir_t0 = ''

## Arquivo com o código principal de time0:
principal_t0 = ''
    
## Arquivo com o código SimAnneal de time0:
simanneal_t0 = ''
    
## Arquivo com o código runfile de time0: (Se não tiver, colar na pasta)
runfile_t0 = 'runfile.sge'

## Arquivo com o resultado de time0:
ParEst_t0 = ''

###############################time1###########################################

## Pasta time1 a ser replicada:
dir_t1 = ''

## Arquivo com o código principal de time1:
principal_t1 = ''
    
## Arquivo com o código SimAnneal de time1:
simanneal_t1 = ''
    
## Arquivo com o código runfile de time1: (Se não tiver, colar na pasta)
runfile_t1 = 'runfile.sge'

## Arquivo com o resultado de time1:
ParEst_t1 = ''


###############################################################################
###############################################################################
###############################################################################
#Não mexer:

batch_t0 = 'batch_'+dir_t0
boots_t0 = dir_t0+'_boot'
path_t0 = 'batch_'+dir_t0+'/'+dir_t0+'_boot'
batch_t1 = 'batch_'+dir_t1
boots_t1 = dir_t1+'_boot'
path_t1 = 'batch_'+dir_t1+'/'+dir_t1+'_boot'

principal_t0 = '/'+principal_t0
simanneal_t0 = '/'+simanneal_t0
runfile_t0 = '/'+runfile_t0
#ParEst_t0 = '/'+ParEst_t0
principal_t1 = '/'+principal_t1
simanneal_t1 = '/'+simanneal_t1
runfile_t1 = '/'+runfile_t1
#ParEst_t1 = '/'+ParEst_t1