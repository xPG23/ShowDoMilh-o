import os

#______________________________________________________________________________

def alerta_erro(codigo):
    from ShowDasFuncoes import user_input
    import os

    os.system('cls')
    print("\n ╔!!═══════════════════════| !ERRO DETECTADO! |═══════════════════════!!╗\n")

    print("   Ops! Algo deu errado durante a execução do jogo.\n")

    if codigo == 1:
        print("    O jogo não foi configurado corretamente.")
        print("     Retornaremos para a tela inicial para corrigir isso.\n")
    else:
        print("    Não foram encontradas perguntas ou respostas válidas.")
        print("     Iniciaremos o processo de configuração novamente.\n")

    print(" ╚^^════════════════════════════════════════════════════════════════^^╝")

    user_input("\n Pressione Enter para continuar...", "string")
    return

#______________________________________________________________________________

def config_inicial():
    from ShowDasFuncoes import cadastrar_perguntas, user_input, lerConfig
    import os

    os.system('cls')

    print("\n ╔^^══════════════════| CONFIGURAÇÃO INICIAL |══════════════════^^╗\n")

    print("   Bem-vindo ao Show do Milhão!")
    print("   Seu objetivo é responder corretamente às perguntas e acumular pontos.")
    print("   Atingindo o topo, você poderá conquistar até R$1.000.000,00!\n")

    nome = user_input("   Digite um nome para seu perfil de jogador: ", "string")
    lerConfig("jogador", nome)

    print("\n  Agora, convide alguém para cadastrar as perguntas do seu jogo.")
    print("  Isso garantirá uma partida personalizada e completa.\n")

    cadastrar_perguntas()

    print("\n   Perguntas configuradas com sucesso!")
    print("  Seja bem-vindo(a) ao Show do Big Corn!\n")

    print(" ╚^^══════════════════════════════════════════════════════════^^╝")

    user_input("\n  Pressione Enter para continuar...", "string")
    return

#______________________________________________________________________________

def loading():
    from ShowDasFuncoes import user_input

    os.system('cls')
    print("""
  ╔oo══════════════════════════════════| LOADING |══════════════════════════════oo╗

      Bem-vindo ao Show do Milhão!

      Neste jogo, você enfrentará uma sequência de perguntas de 
      conhecimentos diversos, divididas em três níveis de dificuldade:
      fácil, médio e difícil.

      A cada resposta correta, você avançará e acumulará prêmios em dinheiro,
      rumo ao grande objetivo: conquistar R$1.000.000,00!

      Você poderá escolher entre:
        • Continuar jogando para multiplicar seus ganhos;
        • Parar e sair com o valor acumulado até o momento;
        • Ou, caso erre uma pergunta, sairá com apenas metade
        do prêmio que tiver conquistado.

      Pense bem antes de decidir.
      Boa sorte, e que comece o Show do Milhão!

  ╚oo═══════════════════════════════════════════════════════════════════════════oo╝
    """)
    user_input("\n   Pressione a tecla Enter para continuar...","string")
    return

#______________________________________________________________________________

def excluindo(escolha):
    from ShowDasFuncoes import info_perguntas,user_input,dificuldade_textual,excluir_perguntas

    os.system('cls')
    while True:
        print(f"\n ╔^^═══════════════════════|EXCLUINDO|═══════════════════════^^╗\n")

        dificuldade,enunciados,_,_,_,_ = info_perguntas(escolha)

        print(f"Deseja excluir essa questão ?: [{dificuldade_textual(dificuldade)}] - {enunciados}")
        opc = user_input("Digita S/N: ","string").upper()

        if opc == 'S':
            excluir_perguntas(escolha)
            break
        elif opc == 'N':
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Opção inválida!")
    print("\n ╚vv═══════════════════════|_________|═══════════════════════vv╝")
    user_input("\nPressione a tecla Enter para continuar...","string")
    
    os.system('cls')
    return

#______________________________________________________________________________

def editando(escolha):
    from ShowDasFuncoes import info_perguntas,user_input,dificuldade_textual,editar_pergunta

    os.system('cls')
    print(f"\n ╔^^═══════════════════════|EDITANDO|═══════════════════════^^╗\n")

    dificuldade,enunciados,alt1,alt2,alt3,resposta = info_perguntas(escolha)
    
    print(f"Dificuldade [{dificuldade_textual(dificuldade)}]\nPergunta:{enunciados}\nResposta:{resposta}\nAlternativa 1:{alt1}\nAlternativa 2:{alt2}\nAlternativa 3:{alt3}\n")

    alternativas =[]
    n_perg = user_input("Nova pergunta: ","string")
    n_resp = user_input("Nova resposta: ","string")
    for i in range(3):
        alternativas.append(user_input(f"Alternativa {i+1}: ","string"))
    alternativas.append(n_resp + "*")

    editar_pergunta(escolha,dificuldade,n_perg,alternativas)
    print("\n ╚vv═══════════════════════|________|═══════════════════════vv╝")
    user_input("\nPressione a tecla Enter para continuar...","string")
    os.system('cls')
    return

#______________________________________________________________________________

def menu_editar_perguntas():
    from ShowDasFuncoes import user_input,pegar_perguntas,dificuldade_textual,ordenar,separar_colunas

    os.system('cls')
    while True:
        perguntas,_ = pegar_perguntas()
        dificuldades,enunciado = separar_colunas(perguntas)
        dificuldades,enunciado = ordenar(dificuldades,enunciado)

        print(f"\n ╔[]═══════════════════════|EDITAR PERGUNTAS|═══════════════════════[]╗\n")
        print(f"    Perguntas [{len(enunciado)}/24]                                     (Minimo:24)\n")
        
        for i,pergunta in enumerate(enunciado):
            print(f"{(i+1):3.0f} - [{dificuldade_textual(dificuldades[i])}] {pergunta}")
        opc = user_input("\n      Digite o número da pergunta para operar ou '0' para voltar: ","int")
        if opc > 0 and opc <= len(enunciado):
            escolha = enunciado[opc - 1]
            indice = opc
            print("\n ╚[]═══════════════════════|________________|═══════════════════════[]╝")
            opc = user_input(f"\n   Digite para | 1 - [Editar] | 2 - [Excluir]  | 0 - [Voltar]: ","int")
            if opc == 1:
                editando(escolha)
            elif opc == 2:
                    dificuldade_escolhida = dificuldades[indice - 1]
                    count_dificuldade = dificuldades.count(dificuldade_escolhida)
                    if len(enunciado) <= 24:
                        os.system('cls')
                        print("Não é possível excluir mais perguntas! (mínimo: 24 no total)")
                        pass
                    elif count_dificuldade <= 8:
                        os.system('cls')
                        print(f"Não é possível excluir mais perguntas de dificuldade '{dificuldade_textual(dificuldade_escolhida)}' (mínimo: 8 por dificuldade).")
                        pass
                    else:
                        excluindo(escolha)
            elif opc == 0:
                os.system('cls')
                pass
            else:
                os.system('cls')
                print("Comando inválido!")
        elif opc == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando inválido!")

#______________________________________________________________________________


def menu_adicionar():
    from ShowDasFuncoes import user_input,salvar_perguntas,pegar_perguntas,separar_colunas

    os.system('cls')
    while True:
        print(f"\n ╔^^═══════════════════════|ADICIONAR PERGUNTA|═══════════════════════^^╗\n")
        perguntas,_ = pegar_perguntas()
        _,enunciado = separar_colunas(perguntas)
        print(f"Perguntas cadastradas: [{len(enunciado)}]\n\n")
        while True:
            qtd = user_input("Digite a quantidade de perguntas que você deseja adicionar, ou '0' para voltar: ", "int")

            if qtd > 0:
                break
            elif qtd == 0:
                os.system('cls')
                return
            else:
                os.system('cls')
                print("Quantidade de perguntas inválidas!")
                print("[ADICIONANDO PERGUNTA] > \n")
                print(f"Perguntas cadastradas: [{len(enunciado)}]\n\n")


        for i in range(qtd):

            print("\nCrie sua nova pergunta preenchendo os campos abaixo: \n")

            print(f"1: Fácil")
            print(f"2: Médio")
            print(f"3: Difícil\n")
            alternativas =[]
            pergunta = []
            while True:
                n_dif = user_input("Digite o número da dificuldade: ","int")

                if n_dif > 0 and n_dif <=3:
                    break
                else:
                    print("Nível de dificuldade inválida")
            n_perg = user_input("Nova pergunta: ","string")
            n_resp = user_input("Nova resposta: ","string")
            linha = []
            for i in range(3):
                linha.append(user_input(f"Alternativa {i+1}: ","string"))
            linha.append(n_resp + "*")
            alternativas.append(linha)
            print()
            pergunta.append((n_dif,n_perg))

            salvar_perguntas(pergunta,alternativas)
            print("Pergunta adicionada com sucesso!")
            while True:
                if qtd > 1:
                    print("\n ╚vv═══════════════════════|__________________|═══════════════════════vv╝")
                    esc = user_input("\nPressione a tecla Enter para continuar... ou '0' para parar!","string")
                    if esc == "0":
                        os.system('cls')
                        return
                    else:
                        os.system('cls')
                        break
                else:
                    print("\n ╚vv═══════════════════════|__________________|═══════════════════════vv╝")
                    user_input("\nPressione a tecla Enter para continuar...","string")
                    os.system('cls')
                    break
            

#______________________________________________________________________________

def menu_recombular():
    from ShowDasFuncoes import user_input,cadastrar_perguntas

    os.system('cls')
    while True:
        print(f"\n ╔[]═══════════════════════|RECOMBULAR|═══════════════════════[]╗\n")
        print("Deseja recombular as perguntas?\n")
        print("""isso fará com que todas as perguntas e respostas já salvas \nsejam apagadas e 
        sobrepostas pelas novas \n\nDigite 'S'(SIM) para confirmação ou 'N'(NÃO) para o retorno.""")
        opc = user_input("Digita uma das opções acima: ","string").upper()
        print(" ╚[]═══════════════════════|__________|═══════════════════════[]╝")

        if opc == "S":
            os.system('cls')
            cadastrar_perguntas()
        elif opc == "N":
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando invalido.")


#______________________________________________________________________________

def menu_perguntas():
    from ShowDasFuncoes import user_input

    os.system('cls')
    while True:
        print(f"\n ╔#═══════════════════════|PERGUNTAS|═══════════════════════#╗\n")
        print("   1 - Editar perguntas ")
        print("   2 - Adicionar perguntas")
        print("   3 - Recombular perguntas")
        print("   0 - Voltar\n")
        print(" ╚#═══════════════════════|_________|═══════════════════════#╝")
        opc = user_input("\n  Digita uma das opções acima: ","int")

        if opc == 1:
            menu_editar_perguntas()
        elif opc == 2:
            menu_adicionar()
        elif opc == 3:
            menu_recombular()
        elif opc == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando inválido!")

#______________________________________________________________________________

def menu_cartas():
    from ShowDasFuncoes import user_input,lerConfig,retorna_bool

    os.system('cls')
    while True:
        cartas = retorna_bool(lerConfig("cartas"))
        if cartas: print("\n   Deseja desativar as cartas? S/N")
        else: print("\n   Deseja ativar as cartas? S/N")
        print("\n\n")
        opc = user_input("\n  Digite uma opção: ", "string")
        if opc.upper() == 'S':
            if cartas:
                lerConfig("cartas",False)
                os.system('cls')
                print("Cartas desativadas!")
                break
            else: 
                lerConfig("cartas",True)
                os.system('cls')
                print("Cartas ativadas!")
                break
        elif opc.upper() == 'N':
            if cartas:
                lerConfig("cartas",True)
                os.system('cls')
                print("Cartas ativadas!")
                break
            else:
                lerConfig("cartas",False)
                os.system('cls')
                print("Cartas desativadas!")
                break
        else:
            os.system('cls')
            print("Opção inválida!")

#______________________________________________________________________________

def menu_pulo():
    from ShowDasFuncoes import user_input,lerConfig,retorna_bool

    os.system('cls')
    while True:
        pulos = retorna_bool(lerConfig("pulos"))
        if pulos: print("\n   Deseja desativar pulos? S/N")
        else: print("\n   Deseja ativar pulos? S/N")
        print("\n\n")
        opc = user_input("\n  Digite uma opção: ", "string")
        if opc.upper() == 'S':
            if pulos:
                lerConfig("pulos",False)
                os.system('cls')
                print("Pulos desativados!")
                break
            else: 
                lerConfig("pulos",True)
                os.system('cls')
                print("Pulos ativados!")
                break
        elif opc.upper() == 'N':
            if pulos:
                lerConfig("pulos",True)
                os.system('cls')
                print("Pulos ativados!")
                break
            else:
                lerConfig("pulos",False)
                os.system('cls')
                print("Pulos desativados!")
                break
        else:
            os.system('cls')
            print("Opção inválida!")


#______________________________________________________________________________

def menu_ajudas():
    from ShowDasFuncoes import user_input

    os.system('cls')
    while True:
        print(f"\n ╔#═══════════════════════|AJUDAS|═══════════════════════#╗\n")
        print("   1 - Cartas ")
        print("   2 - Pulos ")
        print("   0 - Voltar \n")
        print(" ╚#═══════════════════════|______|═══════════════════════#╝")
        opc = user_input("\nDigita uma das opções acima: ","int")

        if opc == 1:
            menu_cartas()
        elif opc == 2:
            menu_pulo()
        elif opc == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando inválido!")

#______________________________________________________________________________

def alterar_nome():
    from ShowDasFuncoes import lerConfig,user_input
    os.system('cls')
    nome = user_input("Digite o nome do novo jogador: ","string")
    lerConfig("jogador",nome)

    print("Nome do jogador alterado!")
    user_input("\nPressione a tecla Enter para continuar...","string")
    os.system('cls')
    return
    
#______________________________________________________________________________    

def menu_nome():
    from ShowDasFuncoes import lerConfig,user_input

    os.system('cls')
    while True:
        print(f"\n ╔#═══════════════════════|NOME DO JOGADOR|═══════════════════════#╗\n")
        print(f"    Jogador atual: {lerConfig("jogador")}\n")
        print("   1 - Alterar jogador ")
        print("   0 - Voltar \n")
        print(" ╚#═══════════════════════|_______________|═══════════════════════#╝")
        opc = user_input("\nDigita uma das opções acima: ","int")

        if opc == 1:
            alterar_nome()
        elif opc == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando inválido!")

#______________________________________________________________________________

def menu_config():
    from ShowDasFuncoes import user_input

    os.system('cls')
    while True:
        print("\n ╔:═══════════════════════|CONFIGURAÇÕES|═══════════════════════:╗\n")
        print("   1 + Cadastro de pergunta ")
        print("   2 + Configuração de ajudas ")
        print("   3 + Alterar jogador ")
        print("   0 + Voltar\n")
        print(" ╚:═══════════════════════|_____________|═══════════════════════:╝")
        opc = user_input("\nDigite uma opção: ","int")

        if opc == 1:
            menu_perguntas()
        elif opc == 2:
            menu_ajudas()
        elif opc == 3:
            menu_nome()
        elif opc == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Comando inválido!")   

#______________________________________________________________________________

def menu_score():
    from ShowDasFuncoes import user_input,caminhoS

    os.system('cls')
    if not os.path.exists(caminhoS):
        print("Ainda não foi registrado nenhum score, jogue para adicionar!\n\n")
        user_input("\nPressione a tecla Enter para continuar...","string") 
        os.system('cls')
        return

    jogadores = []
    print("[_*_*_ - Placar - _*_*__]")
    print("\n ╔:═══════════════════════|PLACAR|═══════════════════════:╗\n")
    with open(caminhoS,'r') as placar:
        for pontos in placar:
            jogadores.append(pontos.strip().split(';'))

    for i,valores in enumerate(jogadores):
        print(f"   {i+1} - {valores[0]}: {valores[1]} pontos")

    print("\n ╚:═══════════════════════|______|═══════════════════════:╝")    
    user_input("\nPressione a tecla Enter para continuar...","string")
    os.system('cls')
    return          

#______________________________________________________________________________

def menu_principal():
    from ShowDasFuncoes import lerConfig,user_input,jogar,verificar_arquivos

    os.system('cls')
    while True:
        print("\n ╔:═══════════════════════|MENU PRINCIPAL|═══════════════════════:╗\n\n")
        print("   1 ═ JOGAR!\n   2 ═ Configurações\n   3 ═ Placar\n   0 ═ Sair\n\n")
        print(f"   versão 1.25                                     Jogador: {lerConfig("jogador")}")
        print(" ╚:═══════════════════════|______________|═══════════════════════:╝")
        opc = user_input("\n   Escolha uma opção: ","int")
    
        if opc == 1:
            verificar_arquivos()
            loading()
            jogar()
        elif opc == 2:
            menu_config()
        elif opc == 3:
            menu_score()
        elif opc == 0:
            break
        else:
           os.system('cls')
           print("Opção inválida!")  

#______________________________________________________________________________

def tela_inicial():
    from ShowDasFuncoes import user_input
    print("""
                       ╔*═══════════════#+-+-+-+-+-+-+-+#════════════════*╗          
                                     _____ __  ______ _       __
                                    / ___// / / / __ \\ |     / /
                                    \\__ \\/ /_/ / / / / | /| / / 
                                   ___/ / __  / /_/ /| |/ |/ /   
                                  /____/_/_/_/\\____/ |__/|__/   
                                        / __ \\/ __ \\\             
                                       / / / / / / //            
                                      / /_/ / /_/ //             
                              __  ___/_____/\\___ //__ /\\//____  
                             /  |/  /  _/ /   / / / ///\\// __ \\ 
                            / /|_/ // // /   / /_/ / _ |/ / / / 
                           / /  / // // /___/ __  / __ / /_/ /  
                          /_/  /_/___/_____/_/ /_/_/ |_\\____/ 
                                                               TM
                   ╚*═══════════════#+-+-+-+-+-+-+-+#════════════════*╝ 
             
                          TM E ©2025 UNIMAR-BCC-C, BRASIL INC.
                Direitos reservados de Sistema Brasileiro de Televisão(SBT) 
                            distribuído por: PG - RA: 2039564
\n""")

    user_input("                         Pressione a tecla Enter para continuar...","string")   
 
#______________________________________________________________________________

def menu_parar(pontos):
    from ShowDasFuncoes import user_input

    os.system('cls')
    while True:
        print(f"Deseja parar com R${pontos}? S/N")
        opc = user_input("Digite uma opção: ", "string")
        if opc.upper() == 'S':
            return True
        elif opc.upper() == 'N':
            return False
        else:
            os.system('cls')
            print("Opção inválida!")
        os.system('cls')    
        return
       
    
#______________________________________________________________________________

def jogo_UI(pontos, pergunta, alternativas, pulos, cartas):
    from ShowDasFuncoes import calcular_pontos, user_input

    valor_pergunta = calcular_pontos(pontos)
    
    print("\n ╔^^═══════════════════════| SHOW DO MILHÃO |═══════════════════════^^╗\n")
    print("   1-4 Alternativas  |  5 - Parar  |  6 - Pular  |  7 - Cartas\n")
    print(f"   Pergunta valendo R${valor_pergunta:,}:")


    print(f"   -> [{pergunta[1]}] {pergunta[0]}?\n")

    for i, alternativa in enumerate(alternativas):
        print(f"    {i + 1} - {str(alternativa).strip('*')}")

    print("\n   ─────────────────────────────────────────────────────────────────────\n")
    print("                              [*  AJUDAS  *]")
 
    if cartas:
        print("                           Cartas disponíveis 🂠")

    print(f"                           Pulos restantes: [{pulos}]\n")

    print("              Resultado se você:")
    print("          ┌────────────┬───────────┬───────────────┐")
    print("          │   Errar    │   Parar   │    Acertar    │")
    print("          ├────────────┼───────────┼───────────────┤")
    print(f"          │   R${(pontos/2):7.0f}│  R${pontos:7.0f}│      R${valor_pergunta:7.0f}│")
    print("          └────────────┴───────────┴───────────────┘")

    print("\n ╚^^════════════════════════════════════════════════════════════════^^╝\n")

    escolha = user_input(" Faça sua escolha: ", "int")
    return escolha

#______________________________________________________________________________

def gameOver(score):
    from ShowDasFuncoes import registrar_score, lerConfig, user_input
    import os

    os.system('cls')
    registrar_score(score, lerConfig("jogador"))

    print("\n   ╔════════════════════════[ FIM DE JOGO ]════════════════════════╗\n")
    
    premio = str(score).replace("1000000", "um MILHÃO de")
    print(f"   Você ganhou {premio} reais!\n")

    if score < 1000:
        print("   Que pena! Tente novamente em outra rodada.")
    elif score < 1000000:
        print("   Parabéns, você jogou muito bem!")
    else:
        print(f"   Aqui temos nosso novo milionário: {lerConfig('jogador')}!")
        print("   Obrigado por jogar!\n")

    print("   ╚══════════════════════════════════════════════════════════════╝")
    user_input("\n   Pressione Enter para continuar...", "string")
    os.system('cls')
    return

#______________________________________________________________________________

