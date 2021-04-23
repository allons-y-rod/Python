#Para Frequencias o Usuário deve escolher entre: rara, baixa, media, alta
#Para Danos o Usuário deve escolher entre: baixos, medios, altos
#Para Importancia o Usuário deve escolher entre: baixa, media, fundamental
#Para VPL o Usuário deve escolher valores diferentes de zero.

#Variaveis de entrada:
frequencia = str(input('Frequência: ')).strip().upper()
danos = str(input('Danos: ')).strip().upper()
importancia = str(input('Importancia: ')).strip().upper()
VPL = float(input('VPL: '))

#Variaveis booleanas
aceitavel=False
inaceitavel=False

#Primeiro rodaremos para danos baixos
if 'BAIXOS' in danos and ('RARA' or 'BAIXA') in frequencia:
    aceitavel = True

if 'BAIXOS' in danos and ('MEDIA' or 'ALTA') in frequencia:
    inaceitavel = True

#Para danos medios
if 'MEDIOS' in danos and 'RARA' in frequencia:
    aceitavel = True

if 'MEDIOS' in danos and ('BAIXA' or 'MEDIA' or 'ALTA') in frequencia:
    inaceitavel = True

#Para danos altos

if 'ALTOS' in danos and ('RARA' or 'BAIXA' or 'MEDIA' or 'ALTA') in frequencia:
    inaceitavel = True

if VPL == 0:
    print('ERRO!! VPL deve estar em valores diferentes de zero')


#Para VPL > 0
#Importancia Fundamental
if (VPL > 0) and (aceitavel or inaceitavel == True) and 'FUNDAMENTAL' in importancia:
    print('Troca Imediata')

#Importancia Media
if (VPL > 0) and (aceitavel == True) and 'MEDIA' in importancia:
    print('Troca a Longo-Prazo')

if (VPL > 0) and (inaceitavel == True) and 'MEDIA' in importancia:
    print('Troca a Medio-Prazo')

#Importancia Baixa

if (VPL > 0) and (aceitavel == True) and 'BAIXA' in importancia:
    print('Não Troca')

if (VPL > 0) and (inaceitavel == True) and 'BAIXA' in importancia:
    print('Troca a Longo-Prazo')

#Para VPL<0
#Importancia Fundamental

if (VPL < 0) and (inaceitavel == True) and 'FUNDAMENTAL' in importancia:
    print('Troca a Medio-Prazo')

if (VPL < 0) and (aceitavel == True) and 'FUNDAMENTAL' in importancia:
    print('Não Troca')

#Importancia Media

if (VPL < 0) and (inaceitavel == True) and 'MEDIA' in importancia:
    print('Troca a Longo-Prazo')

if (VPL < 0) and (aceitavel == True) and 'MEDIA' in importancia:
    print('Não Troca')

#importancia Baixa

if (VPL < 0) and (inaceitavel == True) and 'BAIXA' in importancia:
    print('Troca a Longo-Prazo')

if (VPL < 0) and (aceitavel == True) and 'BAIXA' in importancia:
    Print('Não troca')
