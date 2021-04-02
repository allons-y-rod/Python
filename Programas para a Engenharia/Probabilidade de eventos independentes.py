from time import sleep
print('='*40)
PA = float(input('\033[1;30;45mInsira a Probabilidade de A:\033[m'))
PB = float(input('\033[1;30;45mInsira a Probabilidade de B:\033[m'))
if PA > 1.0 or PB > 1.0:
    print('\033[1;30;41mErro!!!! Os valores inseridos devem estar entre 0 e 1.\033[m')
else:
    print('\033[1;30;45mCARREGANDO...\033[m')
print('='*40)
sleep(1)
PA_e_B = (PA * PB)
PA_ou_B = (PA + PB - PA_e_B)
PA_xou_B = PA * (1 - PB) + (1 - PA) * PB
if PB > 1 and PA > 1:
    print('\033[1;30;41mErro!!!! O valor inserido deve estar entre 0 e 1.\033[m')
if PA <= 1 and PB <= 1:
    print('\033[1;30;45mCom esses valores para A e B, temos:\033[m')
    print('\033[1;30;45mPA^B = {:.4f}\033[m'.format(PA_e_B))
    print('\033[1;30;45mPAvB = {:.4f}\033[m'.format(PA_ou_B))
    print('\033[1;30;45mPAØB = {:.4f}\033[m'.format(PA_xou_B))