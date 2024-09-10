# Definição dos pesos para diferentes tipos de problemas
PESOF = 1
PESOM = 2
PESOD = 3

# Inicialização das variáveis de pontuação para cada equipe e tipo de problema
PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5 = 0, 0, 0, 0, 0
PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5 = 0, 0, 0, 0, 0
PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5 = 0, 0, 0, 0, 0

# Função para cadastrar ou atualizar equipes
def CadastrarEquipe():
    global equipe1, equipe2, equipe3, equipe4, equipe5

    # Verifica se já existem equipes cadastradas
    if Verify() == True:
        resp = True
        while resp == True:
            # Mostra as equipes cadastradas e permite alterar
            print("\\Equipes já cadastradas//\n1."+equipe1+"\n2."+equipe2+"\n3."+equipe3+"\n4."+equipe4+"\n5."+equipe5)
            actionCE = input("Tecle ENTER para sair ou o número da equipe que deseja mudar: ")
            if actionCE == "1":
                equipe1 = input("Nome da primeira equipe: ")
            elif actionCE == "2":
                equipe2 = input("Nome da segunda equipe: ")
            elif actionCE == "3":
                equipe3 = input("Nome da terceira equipe: ")
            elif actionCE == "4":
                equipe4 = input("Nome da quarta equipe: ")
            elif actionCE == "5":
                equipe5 = input("Nome da quinta equipe: ")
            else: resp = False

    # Se não houver equipes cadastradas, solicita os nomes das equipes
    if Verify() == False:
        equipe1 = input("Nome da primeira equipe: ")
        equipe2 = input("Nome da segunda equipe: ")
        equipe3 = input("Nome da terceira equipe: ")
        equipe4 = input("Nome da quarta equipe: ")
        equipe5 = input("Nome da quinta equipe: ")

# Função para registrar a pontuação das equipes
def RegistrarPontuacao():
    global PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5
    global PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5
    global PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5
    global equipe1, equipe2, equipe3, equipe4, equipe5

    # Verifica se as equipes estão cadastradas
    if Verify() == True:
        resp = True
        while resp == True:
            # Mostra as equipes cadastradas e permite registrar a pontuação
            print("\\Equipes cadastradas//\n1."+equipe1+"\n2."+equipe2+"\n3."+equipe3+"\n4."+equipe4+"\n5."+equipe5)
            actionRP = input("Tecle ENTER para sair ou escolha a equipe para registrar a pontuação: ")
            try:
                if actionRP == "1":
                    PontosF_E1 = int(input("Quantidade de problemas fáceis resolvidos: "))
                    PontosM_E1 = int(input("Quantidade de problemas médios resolvidos: "))
                    PontosD_E1 = int(input("Quantidade de problemas difíceis resolvidos: "))
                elif actionRP == "2":
                    PontosF_E2 = int(input("Quantidade de problemas fáceis resolvidos: "))
                    PontosM_E2 = int(input("Quantidade de problemas médios resolvidos: "))
                    PontosD_E2 = int(input("Quantidade de problemas difíceis resolvidos: "))
                elif actionRP == "3":
                    PontosF_E3 = int(input("Quantidade de problemas fáceis resolvidos: "))
                    PontosM_E3 = int(input("Quantidade de problemas médios resolvidos: "))
                    PontosD_E3 = int(input("Quantidade de problemas difíceis resolvidos: "))
                elif actionRP == "4":
                    PontosF_E4 = int(input("Quantidade de problemas fáceis resolvidos: "))
                    PontosM_E4 = int(input("Quantidade de problemas médios resolvidos: "))
                    PontosD_E4 = int(input("Quantidade de problemas difíceis resolvidos: "))
                elif actionRP == "5":
                    PontosF_E5 = int(input("Quantidade de problemas fáceis resolvidos: "))
                    PontosM_E5 = int(input("Quantidade de problemas médios resolvidos: "))
                    PontosD_E5 = int(input("Quantidade de problemas difíceis resolvidos: "))
                else: resp = False
            except:
                print("Preencha as PONTUAÇÕES apenas com números.")
                input("Tecle ENTER para continuar.")
                continue

# Função para registrar o tempo gasto por cada equipe
def RegistrarTempo():
    global tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5
    resp = True
    while resp == True:
        # Mostra as equipes cadastradas e permite registrar o tempo
        try:
            print("\\Equipes cadastradas//\n1."+equipe1+"\n2."+equipe2+"\n3."+equipe3+"\n4."+equipe4+"\n5."+equipe5)
            actionRP = input("Tecle ENTER para sair ou escolha a equipe para registrar o tempo: ")
            if actionRP == "1":
                tempo_E1 = Tempo()
            elif actionRP == "2":
                tempo_E2 = Tempo()
            elif actionRP == "3":
                tempo_E3 = Tempo()
            elif actionRP == "4":
                tempo_E4 = Tempo()
            elif actionRP == "5":
                tempo_E5 = Tempo()
            else: resp = False
        except:
            resp = False
            print("Você não cadastrou equipes.")
            input("Tecle ENTER para continuar.")

# Função para gerar o relatório final com base nas pontuações e tempos registrados
def GerarRelatorio():
    try:
        global PontosF_E1, PontosF_E2, PontosF_E3, PontosF_E4, PontosF_E5
        global PontosM_E1, PontosM_E2, PontosM_E3, PontosM_E4, PontosM_E5
        global PontosD_E1, PontosD_E2, PontosD_E3, PontosD_E4, PontosD_E5
        global equipe1, equipe2, equipe3, equipe4, equipe5
        global tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5

        # Conversão das pontuações para string para exibição
        PF1, PF2, PF3, PF4, PF5 = str(PontosF_E1), str(PontosF_E2), str(PontosF_E3), str(PontosF_E4), str(PontosF_E5)
        PM1, PM2, PM3, PM4, PM5 = str(PontosM_E1), str(PontosM_E2), str(PontosM_E3), str(PontosM_E4), str(PontosM_E5)
        PD1, PD2, PD3, PD4, PD5 = str(PontosD_E1), str(PontosD_E2), str(PontosD_E3), str(PontosD_E4), str(PontosD_E5)

        # Conversão dos nomes das equipes e tempos para string
        ER1, ER2, ER3, ER4, ER5 = equipe1, equipe2, equipe3, equipe4, equipe5
        TEMP1, TEMP2, TEMP3, TEMP4, TEMP5 = tempo_E1, tempo_E2, tempo_E3, tempo_E4, tempo_E5

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
        print("----------------------//RANKING\\----------------------")
        print("1° Lugar: " +ER1+ " com " +str(Ranking1)+ " pontos. Problemas: Fácil: " +PF1+ " Médio: " +PM1+ " Difícil: " +PD1+ ".")
        print("2° Lugar: " +ER2+ " com " +str(Ranking2)+ " pontos. Problemas: Fácil: " +PF2+ " Médio: " +PM2+ " Difícil: " +PD2+ ".")
        print("3° Lugar: " +ER3+ " com " +str(Ranking3)+ " pontos. Problemas: Fácil: " +PF3+ " Médio: " +PM3+ " Difícil: " +PD3+ ".")
        print("4° Lugar: " +ER4+ " com " +str(Ranking4)+ " pontos. Problemas: Fácil: " +PF4+ " Médio: " +PM4+ " Difícil: " +PD4+ ".")
        print("5° Lugar: " +ER5+ " com " +str(Ranking5)+ " pontos. Problemas: Fácil: " +PF5+ " Médio: " +PM5+ " Difícil: " +PD5+ ".")

        # Exibe o tempo gasto da equipe vencedora
        print("A equipe " +ER1+ " gastou " +TEMP1+ " minutos.")
        
        input()
    except:
        print("Verifique se preencheu corretamente as EQUIPES, as PONTUAÇÕES e os TEMPOS")
        input("Tecle ENTER para continuar.")
        menu()

# Função para verificar se pelo menos uma equipe foi cadastrada
def Verify():
    try:
        if equipe1 or equipe2 or equipe3 or equipe4 or equipe5:
            return True
    except NameError:
        return False


# Função para registrar o tempo gasto em um formato específico
def Tempo():
    sequenciaHora = 0
    sequenciaMinuto = 0
    sequenciaSegundo = 0
    tempoTotal = 0
    resp_tempo = True
    while resp_tempo:
        var_temp = input("Tecle Enter para sair ou insira o tempo neste formato hh:mm:ss\n")
        if var_temp == "":
            resp_tempo = False
        elif len(var_temp) == 8:
            try:
                 # Adiciona o tempo fornecido à sequência total
                sequenciaHora += int(var_temp[0:2])
                sequenciaMinuto += int(var_temp[3:5])
                sequenciaSegundo += int(var_temp[6:8])

                # Calcula o tempo total em minutos e segundos
                segundosParaMinutos = sequenciaSegundo // 60
                segundosRestantes = sequenciaSegundo % 60

                tempoMinutos = (sequenciaHora * 60) + sequenciaMinuto + segundosParaMinutos
                tempoTotal = str(tempoMinutos) + " minutos e " + str(segundosRestantes) + " segundos."
                print(tempoTotal)
            except:
                 # Trata erros de formato de entrada
                sequenciaHora = 0
                sequenciaMinuto = 0
                sequenciaSegundo = 0
                segundosParaMinutos = 0
                segundosRestantes = 0
                tempoMinutos = 0
                tempoTotal = 0
                print("Formato Inválido.")
                input("Tecle ENTER para continuar.")
        else:
            print("Formato Inválido.")
            input("Tecle ENTER para continuar.")
    return tempoTotal
    
# Função para exibir o menu principal e chamar as funções apropriadas
def menu():    
    print("=============// Menu //=============")
    print("1.Cadastrar Equipe. \n2.Registrar Pontuação. \n3.Registrar Tempo. \n4.Gerar Relatório.")
    print("====================================")
    action = input("Digite a opção que deseja: ")
    if action == '1':
        CadastrarEquipe()
    elif action == '2':
        RegistrarPontuacao()
    elif action == '3':
        RegistrarTempo()
    elif action == '4':
        GerarRelatorio()
    else: 
        print("Opção inserida não existe.")
        input("Tecle ENTER para continuar.")
    menu()

# Início do programa
menu()