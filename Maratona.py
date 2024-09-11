# Inicialização das variáveis de peso para diferentes tipos de problemas
PESOF = 0
PESOM = 0
PESOD = 0

# Inicialização das variáveis de quantidade de problemas para cada tipo 
QUANTIDADEF = 0
QUANTIDADEM = 0
QUANTIDADED = 0

# Inicialização das variáveis de pontuação para cada equipe e tipo de problema
PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5 = 0, 0, 0, 0, 0
PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5 = 0, 0, 0, 0, 0
PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5 = 0, 0, 0, 0, 0

# Inicialização das variáveis de tempo para cada equipe
tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5 = 0, 0, 0, 0, 0

# Função para cadastrar ou atualizar equipes
def CadastrarEquipe():
    global equipe1, equipe2, equipe3, equipe4, equipe5
    
    equipe1 = input("Nome da primeira equipe: ")
    equipe2 = input("Nome da segunda equipe: ")
    equipe3 = input("Nome da terceira equipe: ")
    equipe4 = input("Nome da quarta equipe: ")
    equipe5 = input("Nome da quinta equipe: ")
    print("\\Equipes cadastradas//\n1."+equipe1+"\n2."+equipe2+"\n3."+equipe3+"\n4."+equipe4+"\n5."+equipe5)
    input("Tecle ENTER para continuar.")

# Função para registrar a pontuação das equipes
def RegistrarPontuacao():
    global PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5
    global PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5
    global PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5
    global equipe1, equipe2, equipe3, equipe4, equipe5
    global tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5

    # Verifica se as equipes estão cadastradas
    resp = True
    while resp == True:
        # Mostra as equipes cadastradas e permite registrar a pontuação
        try:
            print("\\Equipes cadastradas//\n1."+equipe1+"\n2."+equipe2+"\n3."+equipe3+"\n4."+equipe4+"\n5."+equipe5)
        except:
            print("Tenha certeza que todas as esquipes foram cadastradas!")
            input("Tecle ENTER para continuar.")
            resp = False
            continue

        actionRP = input("Tecle ENTER para sair ou escolha a equipe para registrar a pontuação: ")
        if actionRP == "":
            resp = False
            continue
        actionProblem = input("Insira o tipo de questão que essa equipe acertou:\n1. Fácil\n2. Médio\n3. Difícil\n")
        try:
            if actionRP == "1":
                if actionProblem == "1":
                    PontosF_E1 += VerificarPontuacao(PontosF_E1, QUANTIDADEF)
                elif actionProblem == "2":
                    PontosM_E1 += VerificarPontuacao(PontosM_E1, QUANTIDADEM)
                elif actionProblem == "3":
                    PontosD_E1 += VerificarPontuacao(PontosD_E1, QUANTIDADED)
                tempo_E1 += Tempo()
            elif actionRP == "2":
                if actionProblem == "1":
                    PontosF_E2 += VerificarPontuacao(PontosF_E2, QUANTIDADEF)
                elif actionProblem == "2":
                    PontosM_E2 += VerificarPontuacao(PontosM_E2, QUANTIDADEM)
                elif actionProblem == "3":
                    PontosD_E2 += VerificarPontuacao(PontosD_E2, QUANTIDADED)
                tempo_E2 += Tempo()
            elif actionRP == "3":
                if actionProblem == "1":
                    PontosF_E3 += VerificarPontuacao(PontosF_E3, QUANTIDADEF)
                elif actionProblem == "2":
                    PontosM_E3 += VerificarPontuacao(PontosM_E3, QUANTIDADEM)
                elif actionProblem == "3":
                    PontosD_E3 += VerificarPontuacao(PontosD_E3, QUANTIDADED)
                tempo_E3 += Tempo()
            elif actionRP == "4":
                if actionProblem == "1":
                    PontosF_E4 += VerificarPontuacao(PontosF_E4, QUANTIDADEF)
                elif actionProblem == "2":
                    PontosM_E4 += VerificarPontuacao(PontosM_E4, QUANTIDADEM)
                elif actionProblem == "3":
                    PontosD_E4 += VerificarPontuacao(PontosD_E4, QUANTIDADED)
                tempo_E4 += Tempo()
            elif actionRP == "5":
                if actionProblem == "1":
                    PontosF_E5 += VerificarPontuacao(PontosF_E5, QUANTIDADEF)
                elif actionProblem == "2":
                    PontosM_E5 += VerificarPontuacao(PontosM_E5, QUANTIDADEM)
                elif actionProblem == "3":
                    PontosD_E5 += VerificarPontuacao(PontosD_E5, QUANTIDADED)
                tempo_E5 += Tempo()
        except:
            print("Opção inválida.")
            input("Tecle ENTER para continuar.")
            continue

# Função para gerar o relatório final com base nas pontuações e tempos registrados
def GerarRelatorio():
    
    global PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5
    global PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5
    global PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5
    global equipe1, equipe2, equipe3, equipe4, equipe5
    global tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5

    try:
        # Conversão das pontuações para string para exibição
        PF1, PF2, PF3, PF4, PF5 = str(PontosF_E1), str(PontosF_E2), str(PontosF_E3), str(PontosF_E4), str(PontosF_E5)
        PM1, PM2, PM3, PM4, PM5 = str(PontosM_E1), str(PontosM_E2), str(PontosM_E3), str(PontosM_E4), str(PontosM_E5)
        PD1, PD2, PD3, PD4, PD5 = str(PontosD_E1), str(PontosD_E2), str(PontosD_E3), str(PontosD_E4), str(PontosD_E5)

        # Atribuição dos nomes das equipes e seus respectivos tempos para váriaveis temporárias
        # com o objetivo de não altera as variáveis originais ao utilizar o algoritmo bubble sort
        ER1, ER2, ER3, ER4, ER5 = equipe1, equipe2, equipe3, equipe4, equipe5
        TEMP1 = Conversor(tempo_E1)
        TEMP2 = Conversor(tempo_E2)
        TEMP3 = Conversor(tempo_E3)
        TEMP4 = Conversor(tempo_E4)
        TEMP5 = Conversor(tempo_E5)

        # Cálculo do Pontuação Total das equipes com base nas pontuações e pesos
        Ranking1 = (PontosF_E1 * PESOF) + (PontosM_E1 * PESOM) + (PontosD_E1 * PESOD)
        Ranking2 = (PontosF_E2 * PESOF) + (PontosM_E2 * PESOM) + (PontosD_E2 * PESOD)
        Ranking3 = (PontosF_E3 * PESOF) + (PontosM_E3 * PESOM) + (PontosD_E3 * PESOD)
        Ranking4 = (PontosF_E4 * PESOF) + (PontosM_E4 * PESOM) + (PontosD_E4 * PESOD)
        Ranking5 = (PontosF_E5 * PESOF) + (PontosM_E5 * PESOM) + (PontosD_E5 * PESOD)

        # Ordena os rankings das equipes em ordem crescente
        if Ranking1 < Ranking2:
            Ranking1, Ranking2 = Ranking2, Ranking1
            ER1, ER2 = ER2, ER1
            PF1, PF2 = PF2, PF1
            PM1, PM2 = PM2, PM1
            PD1, PD2 = PD2, PD1
            TEMP1, TEMP2 = TEMP2, TEMP1
        if Ranking1 < Ranking3:
            Ranking1, Ranking3 = Ranking3, Ranking1
            ER1, ER3 = ER3, ER1
            PF1, PF3 = PF3, PF1
            PM1, PM3 = PM3, PM1
            PD1, PD3 = PD3, PD1
            TEMP1, TEMP3 = TEMP3, TEMP1
        if Ranking1 < Ranking4:
            Ranking1, Ranking4 = Ranking4, Ranking1
            ER1, ER4 = ER4, ER1
            PF1, PF4 = PF4, PF1
            PM1, PM4 = PM4, PM1
            PD1, PD4 = PD4, PD1
            TEMP1, TEMP4 = TEMP4, TEMP1
        if Ranking1 < Ranking5:
            Ranking1, Ranking5 = Ranking5, Ranking1
            ER1, ER5 = ER5, ER1
            PF1, PF5 = PF5, PF1
            PM1, PM5 = PM5, PM1
            PD1, PD5 = PD5, PD1
            TEMP1, TEMP5 = TEMP5, TEMP1
        if Ranking2 < Ranking3:
            Ranking2, Ranking3 = Ranking3, Ranking2
            ER2, ER3 = ER3, ER2
            PF2, PF3 = PF3, PF2
            PM2, PM3 = PM3, PM2
            PD2, PD3 = PD3, PD2
            TEMP2, TEMP3 = TEMP3, TEMP2
        if Ranking2 < Ranking4:
            Ranking2, Ranking4 = Ranking4, Ranking2
            ER2, ER4 = ER4, ER2
            PF2, PF4 = PF4, PF2
            PM2, PM4 = PM4, PM2
            PD2, PD4 = PD4, PD2
            TEMP2, TEMP4 = TEMP4, TEMP2
        if Ranking2 < Ranking5:
            Ranking2, Ranking5 = Ranking5, Ranking2
            ER2, ER5 = ER5, ER2
            PF2, PF5 = PF5, PF2
            PM2, PM5 = PM5, PM2
            PD2, PD5 = PD5, PD2
            TEMP2, TEMP5 = TEMP5, TEMP2
        if Ranking3 < Ranking4:
            Ranking3, Ranking4 = Ranking4, Ranking3
            ER3, ER4 = ER4, ER3
            PF3, PF4 = PF4, PF3
            PM3, PM4 = PM4, PM3
            PD3, PD4 = PD4, PD3
            TEMP3, TEMP4 = TEMP4, TEMP3
        if Ranking3 < Ranking5:
            Ranking3, Ranking5 = Ranking5, Ranking3
            ER3, ER5 = ER5, ER3
            PF3, PF5 = PF5, PF3
            PM3, PM5 = PM5, PM3
            PD3, PD5 = PD5, PD3
            TEMP3, TEMP5 = TEMP5, TEMP3
        if Ranking4 < Ranking5:
            Ranking4, Ranking5 = Ranking5, Ranking4
            ER4, ER5 = ER5, ER4
            PF4, PF5 = PF5, PF4
            PM4, PM5 = PM5, PM4
            PD4, PD5 = PD5, PD4
            TEMP4, TEMP5 = TEMP5, TEMP4

        # Exibe o relatório com o ranking das equipes, os tempos gastos e a quantidade de problemas resolvidos de cada tipo
        print("-----------------------------//RANKING\\-----------------------------")
        print("1° Lugar: " +ER1+ " com " +str(Ranking1)+ " pontos. Problemas: Fácil: " +PF1+ " Médio: " +PM1+ " Difícil: " +PD1+ ".")
        print("2° Lugar: " +ER2+ " com " +str(Ranking2)+ " pontos. Problemas: Fácil: " +PF2+ " Médio: " +PM2+ " Difícil: " +PD2+ ".")
        print("3° Lugar: " +ER3+ " com " +str(Ranking3)+ " pontos. Problemas: Fácil: " +PF3+ " Médio: " +PM3+ " Difícil: " +PD3+ ".")
        print("4° Lugar: " +ER4+ " com " +str(Ranking4)+ " pontos. Problemas: Fácil: " +PF4+ " Médio: " +PM4+ " Difícil: " +PD4+ ".")
        print("5° Lugar: " +ER5+ " com " +str(Ranking5)+ " pontos. Problemas: Fácil: " +PF5+ " Médio: " +PM5+ " Difícil: " +PD5+ ".")
        print("--------------------------------------------------------------------")
        # Exibe o tempo gasto da equipe vencedora
        print("A equipe " +ER1+ " foi a VENCEDORA e gastou " + TEMP1 + " .")
        
        input()
    except:
        print("Verifique se preencheu corretamente as EQUIPES, as PONTUAÇÕES e os TEMPOS")
        input("Tecle ENTER para continuar.")
        menu()


# Função para registrar o tempo em centésimos o que facilita a comparação de resultado
def Tempo():
    print("Agora insira o tempo que a equipe levou para concluir o problema.")
    resp = True
    while resp == True:
        try:
            minutos = int(input("Insira os minutos primeiro: "))
            segundos = int(input("Insira os segundos: "))
            centesimos = int(input("Insira os centésimos de segundo (Menor valor válido = 0): "))
            resp = False
        except:
            print("Insira os tempo corretamente!")
            input("Tecle ENTER para continuar.")
            continue
    tempoTotal = minutos * 60 * 100 + segundos * 100 + centesimos
    return tempoTotal

# Função para converter o tempo de centésimos para o formato minutos/segundos/centésimos
def Conversor(x):
    minutos = int(x/(60*100))
    segundos = int((x/(60*100) - minutos) * 60)
    centesimos = int(((x/(60*100) - minutos) * 60 - segundos) * 100)
    tempoTotalExibicao = str(minutos) + " minutos, " + str(segundos) + " segundos e " + str(centesimos) + " centesimos"
    return tempoTotalExibicao

#Verificador de pontuação para não permitir que se atribua pontos além do limite estabelecido
def VerificarPontuacao(pontos, limite):
    if pontos >= limite:
        print("A equipe não pode mais resolver problemas deste tipo, a pontuação não será atribuida!")
        return 0
    else:
        return 1
    
# Função para Registrar o peso das quetões e a quantidade de cada tipo
def RegistrarQuestoes():

    global PESOF, PESOM, PESOD
    global QUANTIDADEF, QUANTIDADEM, QUANTIDADED

    print("======// Registrar Questões //======")
    print("1.Registrar Peso. \n2.Registrar Quantidade.")
    print("====================================")
    actionRQ = input("Tecle ENTER para sair ou Digite a opção que deseja: ")
    if actionRQ == "1":
        try:
            PESOF = int(input("Insira o peso das questões fáceis: "))
            PESOM = int(input("Insira o peso das questões médias: "))
            PESOD = int(input("Insira o peso das questões difíceis: "))
            print()
            print("Pesos dos problemas registrados com sucesso!")
            input("Tecle ENTER para continuar")
        except:
            print("Valores inválidos.")
            input("Tecle ENTER para continuar.")
    elif actionRQ == "2":
        try:
            print("A quantidade de problemas não pode passar de 5!")
            QUANTIDADEF = int(input("Insira a quantidade de problemas fáceis: "))
            QUANTIDADEM = int(input("Insira a quantidade de problemas médios: "))
            QUANTIDADED = int(input("Insira a quantidade de problemas difíceis: "))
            verify = QUANTIDADEF + QUANTIDADEM + QUANTIDADED
            if verify != 5:
                QUANTIDADEF = 0
                QUANTIDADEM = 0
                QUANTIDADED = 0
                raise Exception()
            print()
            print("Quantidade de problemas registrada com sucesso!")
            input("Tecle ENTER para continuar")
        except:
            print("Tenha a certeza de digitar apenas números e que a quantidade de problemas seja igual a 5!")
            input("Tecle ENTER para continuar.")
    elif actionRQ == "":
        print()

def ConsultarDados():
    global PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5
    global PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5
    global PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5
    global equipe1, equipe2, equipe3, equipe4, equipe5
    global tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5
    global PESOF, PESOM, PESOD
    global QUANTIDADEF, QUANTIDADEM, QUANTIDADED

    print("=============// Consulta de Dados //=============")
    print("Escolha o tipo de dado a ser consultado: ")
    print("1. Nome de Equipe")
    print("2. Pesos e Quantidades de problemas")
    print("3. Pontuações")
    print("4. Tempo")
    print("=================================================")
    actionConsulta = input()
    try:
        if actionConsulta == "1":
            print("1." + equipe1 + "\n2." + equipe2 + "\n3." + equipe3 + "\n4." + equipe4 + "\n5." + equipe5)
            input()
        elif actionConsulta == "2":
            print("Pesos. Fácil: " + str(PESOF) + "; Médio: " + str(PESOM) + "; Difícil: " + str(PESOD) + ".")
            print("Quantidades. Fácil: " + str(QUANTIDADEF) + "; Médio: " + str(QUANTIDADEM) + "; Difícil: " + str(QUANTIDADED) + ";")
            input()
        elif actionConsulta == "3":
            print("Equipe "+ equipe1 + ". Fácil: " + str(PontosF_E1) + "; Médio: " + str(PontosM_E1) + "; Difícil: " + str(PontosD_E1) +".")
            print("Equipe "+ equipe2 + ". Fácil: " + str(PontosF_E2) + "; Médio: " + str(PontosM_E2) + "; Difícil: " + str(PontosD_E2) +".")
            print("Equipe "+ equipe3 + ". Fácil: " + str(PontosF_E3) + "; Médio: " + str(PontosM_E3) + "; Difícil: " + str(PontosD_E3) +".")
            print("Equipe "+ equipe4 + ". Fácil: " + str(PontosF_E4) + "; Médio: " + str(PontosM_E4) + "; Difícil: " + str(PontosD_E4) +".")
            print("Equipe "+ equipe5 + ". Fácil: " + str(PontosF_E5) + "; Médio: " + str(PontosM_E5) + "; Difícil: " + str(PontosD_E5) +".")
            input()
        elif actionConsulta == "4":
            print("Tempo equipe " + equipe1 + ": " + Conversor(tempo_E1))
            print("Tempo equipe " + equipe2 + ": " + Conversor(tempo_E2))
            print("Tempo equipe " + equipe3 + ": " + Conversor(tempo_E3))
            print("Tempo equipe " + equipe4 + ": " + Conversor(tempo_E4))
            print("Tempo equipe " + equipe5 + ": " + Conversor(tempo_E5))
            input()
    except ValueError:
        print("Não foi possível realizar a ação desejada.")
        print("Tecle ENTER para continuar.")

# Função para exibir o menu principal e chamar as funções apropriadas
def menu():    
    while True:
        print("=============// Menu //=============")
        print("1.Cadastrar Equipe. \n2.Registrar Questões. \n3.Registrar Pontuação. \n4.Consultar Dados.\n5.Gerar Relatório.\n6.Sair.")
        print("====================================")
        action = input("Digite a opção que deseja: ")
        if action == '1':
            CadastrarEquipe()
        elif action == '2':
            RegistrarQuestoes()
        elif action == '3':
            RegistrarPontuacao()
        elif action == '4':
            ConsultarDados()
        elif action == '5':
            GerarRelatorio()
        elif action == '6':
            print("Saindo...")
            break
        else: 
            print("Opção inserida não existe.")
            input("Tecle ENTER para continuar.")

# Início do programa
menu()