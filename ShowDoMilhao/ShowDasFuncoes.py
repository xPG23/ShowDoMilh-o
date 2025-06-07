import os
from random import randint
from ShowDosMenus import jogo_UI,gameOver,alerta_erro,menu_parar

path = "Game_Config/config.txt"
caminhoS = "Game_Config/placar.txt"
caminhoP = "Game_Config/perguntas.txt"
caminhoR = "Game_Config/respostas.txt"

#______________________________________________________________________________

def retorna_bool(valor):

    if valor == "True":
        return True
    else:
        return False

#______________________________________________________________________________

def user_input(string : str, tipo : str):
    
    while True:
            if tipo.lower() == "int":
               try:
                   return int(input(string))
               except:
                    print("   Tipo errado tente novamente!")
                    continue                    
            elif tipo.lower() == "float":
                try:
                    return float(input(string))
                except:
                    print("   Tipo errado tente novamente!")
                    continue 
            elif tipo.lower() == "string":
                try:
                    return input(string)
                except:
                    print("   Tipo errado tente novamente!")
                    continue 
            else:
                print("Tipo errado altere o parâmetro da função!")
                break

#______________________________________________________________________________

def embaralhar(lista):

    matx = []
    for i in range(len(lista)):
        matx.append(None)

    while True:
        index = randint(0,len(matx) - 1)
        if matx[index] == None:
            alternativa = lista[randint(0,len(lista)-1)]
            if alternativa not in matx:
                matx[index] = alternativa
            else:
                alternativa = lista[randint(0,len(lista)-1)]
        else:
            index = randint(0,3)

        if not None in matx:
            return matx
        
#______________________________________________________________________________        

def ordenar(lista1,lista2 = None,modo : str = None):

    if modo != "dcrs" and modo != None:
        print("Debug> Modo de ordenação inválido!")
        return

    ordenados = []
    segmento = []
    for c,valor in enumerate(lista1):
        inserido = False
        for i in range(len(ordenados)):
            if modo == None:
                if valor < ordenados[i]:
                    ordenados.insert(i, valor)
                    if lista2:
                        segmento.insert(i, lista2[c])
                    inserido = True
                    break
            else:
                if valor > ordenados[i]:
                    ordenados.insert(i, valor)
                    if lista2:
                        segmento.insert(i, lista2[c])
                    inserido = True
                    break
        if not inserido:
            ordenados.append(valor)
            if lista2:
                segmento.append(lista2[c])


    if lista2 == None:
        return ordenados
    else:
        return ordenados,segmento

#______________________________________________________________________________      

def primeira_jogada():
     with open(path, 'w') as gameConfig:
        gameConfig.write("pj;True"+ '\n' + "pulos;True" + '\n' + "cartas;True" +' \n' +"jogador;None")
        return True    

#______________________________________________________________________________      

def separar_colunas(lista_pai, separador=";"):

    colunas = []

    for linha in lista_pai:
        partes = linha.strip().split(separador)

        if not colunas:
            colunas = [[] for _ in partes]

        for i, valor in enumerate(partes):
            colunas[i].append(valor)

    return tuple(colunas)

#*******************************dependência************************************ 
def chaves_valores(path):

    if not os.path.exists(path):
        primeira_jogada(path)

    with open(path, "r") as arquivo:
        linhas = arquivo.readlines()

    return separar_colunas(linhas)

#*******************************dependência************************************
def lerConfig(chave: str, valor=None): #Conceito de tupla e olhar bem a identação

    with open(path, "r") as arquivo:
        linhas = arquivo.readlines()
 
    chaves, valores = chaves_valores(path)

    if valor == None:
        for i,chav in enumerate(chaves):
            if chav == chave:
                return valores[i]
        print("Debug: Chave não encontrada!")
        return   
    
    novo_conteudo = []
    
    for i,chav in enumerate(chaves):
        if  chav == chave:
            novo_conteudo.append(f"{chave};{str(valor)}\n")
        else:
            novo_conteudo.append(linhas[i])

    if len(novo_conteudo) != 0:      
        with open(path, "w") as arquivo:
            arquivo.writelines(novo_conteudo)
            return novo_conteudo  
    else:           
        print("Debug: Chave não encontrada!")
        return     

#______________________________________________________________________________      

def cadastrar_jogador(nome):
    lerConfig("jogador",nome) 

#______________________________________________________________________________

def selecionar_dificuldade(dificuldades):
    while True:
        print("\nSelecione a dificuldade:")
        print(f"1: Fácil (Cadastradas: {dificuldades[0]}/8)")
        print(f"2: Médio (Cadastradas: {dificuldades[1]}/8)")
        print(f"3: Difícil (Cadastradas: {dificuldades[2]}/8)")

        escolha = user_input("Digite o número da dificuldade: ","int")

        escolha = int(escolha)
        if escolha > 0 and escolha <= 3:
            if dificuldades[escolha - 1] < 8:
                return escolha
            else:
                print("Limite de 8 perguntas já atingido para essa dificuldade.")
        else:
            print("Escolha inválida!")

#______________________________________________________________________________

def excluir_perguntas(questao):
    if not os.path.exists(caminhoP) or not os.path.exists(caminhoR):
        alerta_erro(1)
        return
    
    perguntas,respostas = pegar_perguntas()

    for i, linha in enumerate(perguntas):
        _, enunciado = linha.strip().split(';', 1)
        if enunciado == questao:
            perguntas.remove(perguntas[i])
            respostas.remove(respostas[i])
            break

    with open(caminhoP, 'w') as dirperg, open(caminhoR, 'w') as dirRespo:
        dirperg.writelines(perguntas)
        dirRespo.writelines(respostas)

    print("Pergunta removida com sucesso!")
    
#*******************************dependência************************************    
def editar_pergunta(enunciado_antigo, dificuldade, nova_pergunta, alternativas):
    if not os.path.exists(caminhoP) or not os.path.exists(caminhoR):
        os.makedirs(os.path.dirname(caminhoP), exist_ok=True)
        os.makedirs(os.path.dirname(caminhoR), exist_ok=True)

    perguntas,respostas = pegar_perguntas()

    for i, linha in enumerate(perguntas):
        _, enunciado = linha.strip().split(';', 1)
        if enunciado == enunciado_antigo:
            indice = i
            break

    difi = dificuldade
    enunciado_novo = nova_pergunta
    perguntas[indice] = f"{difi};{enunciado_novo}\n"
    respostas[indice] = ";".join(alternativas) + "\n"

    with open(caminhoP, 'w') as dirperg, open(caminhoR, 'w') as dirRespo:
        dirperg.writelines(perguntas)
        dirRespo.writelines(respostas)

    print("\nPergunta editada com sucesso!")

#*******************************dependência************************************
def salvar_perguntas(perguntas, respostas):
    if not os.path.exists(caminhoP) or not os.path.exists(caminhoR):
        os.makedirs(os.path.dirname(caminhoP), exist_ok=True)
        os.makedirs(os.path.dirname(caminhoR), exist_ok=True)

    with open(caminhoP, 'a+') as dirPerg, open(caminhoR, 'a+') as dirRespo:
        for dificuldade, enunciado in perguntas:
            dirPerg.write(f"{dificuldade};{enunciado}\n")  

        for alternativas in respostas:
            linha = ";".join(alternativas)  
            dirRespo.write(f"{linha}\n")

#*******************************dependência************************************
def cadastrar_perguntas():
    print("O jogo funciona com a base de 16 questões + as questões para o caso de utilizar os pulos\ntotalizando 24 questões!")

    pergunta = []   
    resposta = []
    dificuldades = [0,0,0]        

    for i in range(24):
        linha = []
        print(f"\nPergunta{i+1}: ")
        enunciado = user_input("Digite o enunciado da pergunta: ", "string")
        dificuldade = selecionar_dificuldade(dificuldades)
        dificuldades[dificuldade - 1] += 1  
        correta = user_input("Digite a resposta correta: ", "string")
        for i in range(3):
            linha.append(user_input(f"Digite a alternativa errada {i+1}: ", "string"))
        linha.append(correta+"*")
        resposta.append(linha)
        pergunta.append([dificuldade,enunciado])

    salvar_perguntas(pergunta,resposta)
    print("\nPerguntas salvas com sucesso!")
    user_input("Pressione ENTER para continuar...","string")    
    return

#*******************************dependência************************************
def verificar_arquivos():
    if not os.path.exists(path) :
        alerta_erro(1)
        cadastrar_perguntas()
        return
    else:
        try:
            with open(caminhoP, "r") as perg, open(caminhoR, "r") as resp:
                perguntas = perg.read()
                respostas = resp.read()

                if not perguntas or not respostas:
                    alerta_erro(2)
                    cadastrar_perguntas()
                    return
                else:
                    return
        except:
            alerta_erro(2)
            cadastrar_perguntas()
            return

#______________________________________________________________________________

def info_perguntas(parametro):
    perguntas,respostas = pegar_perguntas()

    dificuldade,enunciados = separar_colunas(perguntas)
    alt1,alt2,alt3,resposta = separar_colunas(respostas)

    for i,enunciado in enumerate(enunciados):
        if enunciado == parametro:
            return dificuldade[i],enunciados[i],alt1[i],alt2[i],alt3[i],resposta[i]

#*******************************dependência************************************
def pegar_perguntas():

    perguntas = []
    respostas = []

    if not os.path.exists(caminhoP) or not os.path.exists(caminhoR):
        os.makedirs(os.path.dirname(caminhoP), exist_ok=True)
        os.makedirs(os.path.dirname(caminhoR), exist_ok=True)

    with open(caminhoP, 'r') as dirPerg, open(caminhoR, 'r') as dirRespo:
        for  pergunta in dirPerg:
            perguntas.append(pergunta)
        for resposta in dirRespo:
            respostas.append(resposta)
            

    return perguntas,respostas

#______________________________________________________________________________

def dificuldade_textual(nivel):
    return "Fácil" if nivel == "1" else "Médio" if nivel == "2" else "Difícil"

#______________________________________________________________________________

def selecionar_pergunta(round, perguntas, respostas,garbageColector = None):

    if round <= 5:
        nivel_dificuldade = "1"
    elif round <= 10:
        nivel_dificuldade = "2"
    else:
        nivel_dificuldade = "3"

    perguntas_filtradas = []
    respostas_filtradas = []

    for i, pergunta in enumerate(perguntas):
        dificuldade, enunciado = pergunta.strip().split(";") 
        if dificuldade == nivel_dificuldade:
            if enunciado not in garbageColector:
                perguntas_filtradas.append((enunciado, dificuldade_textual(dificuldade)))
                respostas_filtradas.append(respostas[i].strip().split(";"))

    if not perguntas_filtradas:
        print("Nenhuma pergunta disponível para essa dificuldade.")
        return None

    index = randint(0, len(perguntas_filtradas) - 1)
    pergunta_selecionada = perguntas_filtradas[index]
    alternativas = respostas_filtradas[index]


    return pergunta_selecionada, embaralhar(alternativas)

#______________________________________________________________________________

def separar_resposta(alternativas):
    for alternativa in alternativas:
        if alternativa[-1] == '*':
            return alternativa
        
#*******************************dependência************************************
def reduzir_lista(n,lista):

    resposta = separar_resposta(lista)
    erradas = []
    
    if n == 3:
        erradas.append(resposta)
        return erradas

    for alternativa in lista:
        if alternativa != resposta:
            erradas.append(alternativa)

    for i in range(n):
        erradas.remove(erradas[i])
    
    erradas.append(resposta)
    return embaralhar(erradas)

#______________________________________________________________________________

def calcular_pontos(pontosAtuais):
    if pontosAtuais == 0:
        return 1000
    elif pontosAtuais <= 4000:
        return pontosAtuais + 1000
    elif pontosAtuais == 5000:
        return pontosAtuais * 2
    elif pontosAtuais <= 40000:
        return pontosAtuais + 10000
    elif pontosAtuais == 50000:
        return pontosAtuais * 2
    elif pontosAtuais <= 400000:
        return pontosAtuais + 100000
    else: return 1000000

#______________________________________________________________________________

def valor_carta(transform):
    if transform[-1] == '♥':
        return 0
    else:
        return int(transform[0])
    
#______________________________________________________________________________

def escolher_cartas():
    cartas = ["1♠","2♦","3♣","K♥"]
    cartas = embaralhar(cartas)
    os.system('cls')
    while True:
        print("Escolha uma carta:\n  1- 🂠 | 2- 🂠 | 3- 🂠 | 4- 🂠 \n")
        escolha = user_input("Escolha: ", "int")
        if escolha == 1:
            os.system('cls')
            print("Sua carta foi:")
            print(f" {cartas[escolha-1]} | 🂠 | 🂠 | 🂠 ")
            user_input("Pressione qualquer tecla para continuar...","string")
            return cartas[escolha-1]
        elif escolha == 2:
            os.system('cls')
            print("Sua carta foi:")
            print(f" 🂠 | {cartas[escolha-1]} | 🂠 | 🂠 ")
            user_input("Pressione qualquer tecla para continuar...","string")
            return cartas[escolha-1]
        elif escolha == 3:
            os.system('cls')
            print("Sua carta foi:")
            print(f" 🂠 | 🂠 | {cartas[escolha-1]} | 🂠 ")
            user_input("Pressione qualquer tecla para continuar...","string")
            return cartas[escolha-1]
        elif escolha == 4: 
            os.system('cls')
            print("Sua carta foi:")
            print(f" 🂠 | 🂠 | 🂠 | {cartas[escolha-1]} ")
            user_input("Pressione qualquer tecla para continuar...","string")
            return cartas[escolha-1]
        else:
            os.system('cls')
            print("Opção selecionada inexistente, tentar novamente!")

#______________________________________________________________________________

def registrar_score(pontos, nome):

    scores = []

    
    if os.path.exists(caminhoS):
        with open(caminhoS, 'r') as pontuacao:
            linha = pontuacao.readlines()
    else:
        with open(caminhoS, "w+") as score:
            score.write(f"{nome};{pontos}")
            return

    n,p = separar_colunas(linha)
    n.append(nome)
    p.append(pontos)

    scores,pontos = ordenar(n,p)

    with open(caminhoS, 'w') as f:
        for i,placar in enumerate(scores):
            f.write(f"{placar};{pontos[i]}\n")

#______________________________________________________________________________

def jogar():
    round = 0
    pontos = 0

    if retorna_bool(lerConfig("pulos")):
        pulos = 3
    else:
        pulos = 0

    cartas = retorna_bool(lerConfig("cartas"))

    garbageColector = []
    listaP , listaR = pegar_perguntas()
    pergunta,alternativas = selecionar_pergunta(round,listaP,listaR,garbageColector)

    os.system('cls')
    while round < 16:
        escolha = jogo_UI(pontos,pergunta,alternativas,pulos,cartas)
        resposta = separar_resposta(alternativas)    
        if escolha > 0 and escolha <= len(alternativas):
            if resposta == alternativas[escolha - 1]:
                garbageColector.append(pergunta[0])
                pontos = calcular_pontos(pontos)
                round += 1
                pergunta,alternativas = selecionar_pergunta(round,listaP,listaR,garbageColector)
                os.system('cls')
                continue
            else:
                break 
        elif escolha == 5:
            opc = menu_parar(pontos)
            if opc:
                break
        elif escolha == 6:
            if pulos != 0:
                pulos -= 1
                garbageColector.append(pergunta[0])
                pergunta,alternativas = selecionar_pergunta(round,listaP,listaR,garbageColector)
                os.system('cls')
                print("Você pulou a questão")
                continue
            else:
                os.system('cls')
                print("Você não tem mais pulos disponiveis")
        elif escolha == 7:
            if cartas != False:
                carta = escolher_cartas()
                valorCarta = valor_carta(carta)
                alternativas = reduzir_lista(valorCarta,alternativas)
                cartas = False
                continue
            else:
                os.system('cls')
                print("Você já usou suas cartas!")
        else:
            os.system('cls')
            print("Escolha inexistente, tente novamente!")
    
    gameOver(pontos)
    return

#______________________________________________________________________________
