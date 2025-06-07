import os
from ShowDasFuncoes import *
from ShowDosMenus import *
from Win10CmdLauncher import *

isPrimeiraJogada = None

#ASFDASFADAS pra dar sorte
os.makedirs(os.path.dirname(path), exist_ok=True)

maximizar_console() #(habilitar somente win10)
letras_grande() #(habilitar somente win10)


if os.path.exists(path):   
    with open(path, 'r') as gameConfig:
        content = gameConfig.readline().strip().split(';')
        if content[1] == "True":
            isPrimeiraJogada = False
            lerConfig("pj",isPrimeiraJogada)
            config_inicial()
        elif len(content) == 0:
            isPrimeiraJogada = primeira_jogada()
else:
    isPrimeiraJogada = primeira_jogada()
    config_inicial()

tela_inicial()
menu_principal()





