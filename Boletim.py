'''
Fudamentos de Programação 2022.1
Trabalho Final em Equipe

Equipe:
Antonio Lisboa De Carvalho
Daniel Vítor Oliveira Nascimento
Gabriel Lucas Silva Rodrigues
Lydiana Rodrigues de Oliveira
Rafael Freitas Dantas

'''
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#--- Função para limpar terminal
def clear(): os.system('cls')
class cortxt:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


#--- Menu de acesso às funcionalidades
def menu():
    print('''
    * * * * * * * * <Projeto X> * * * * * * * *
    *      - Cadastrar turma : 1              *
    *                                         *
    *      - Acessar turma já cadastrada : 2  *
    *                                         *
    *      - Fechar o programa : 0            *
    * * * * * * * * * * * * * * * * * * * * * *''')


#------ Entrada de dados
#------
# dados sobre a disciplina: nome da disciplina, qte créditos, num alunos matriculados, qte de avaliações
#------
def cadastroTurma(dicionarioTurma, dicionarioCadastros):
    clear()
    print('''
    ******** <Cadastro De Turma> ********''')

    nomeDis = str(input("    *  - Nome da disciplina: "))
    dicionarioTurma['nome disciplina'] = nomeDis
    
    creditos = int(input("    *  - Quantidade de créditos: "))
    dicionarioTurma['créditos'] = creditos

    quantAlunos = int(input("    *  - Número de alunos matriculados: "))
    dicionarioTurma['número de alunos'] = quantAlunos

    quantAvaliacoes = int(input("    *  - Quantidade de avaliações: "))
    dicionarioTurma['Qte avaliações'] = quantAvaliacoes

    print('''    *                                   *
    *************************************''')

    dicionarioCadastros[nomeDis] = {}
    dicionarioCadastros[nomeDis]['dado turma'] = dicionarioTurma


#------
# dados sobre os alunos: nome, qte faltas, notas
#------
def cadastroaluno(dicionarioAlunos, dicionarioTurma, dicionarioCadastros):

    numeroDeAlunos = int(input("Insira quantos alunos deseja cadastrar?: "))  
    j = 1

    while j <= numeroDeAlunos:

        nome = str(input(f"Insira o nome do aluno {j}: "))
        if nome in dicionarioAlunos:  #verifica dentro das chaves do dicionário se aluno com esse nome já foi cadastrado
            print('Esse aluno já foi cadastrado! Cadastre um novo aluno.')
            nome = str(input(f"Insira o nome do aluno {j}: "))

        matricula = int(input('Insira o número da matricula do aluno: '))
        faltas = int(input("Insira o número de faltas do aluno: "))

        quantidadeNotas = dicionarioTurma['Qte avaliações']  #acessa a quantidade de provas cadastrado anteriormente
        notas = []  #lista para armazenar notas do aluno

        i=1
        while i <= quantidadeNotas:
            n = float(input(f"Qual a nota {i}? "))
            notas.append(n)
            i += 1

        #cálculo da média do aluno
        media = round(np.average(notas), 1)

        #cálculo da assiduidade do aluno
        if dicionarioTurma['créditos'] == 2:
            presença = 32 - faltas
            freq = round(((presença*100)/32), 1)  #dado em porcentagem
        elif dicionarioTurma['créditos'] == 4:
            presença = 64 - faltas
            freq = round(((presença*100)/64), 1)  #dado em porcentagem
        elif dicionarioTurma['créditos'] == 6:
            presença = 96 - faltas
            freq = round(((presença*100)/96), 1)  #dado em porcentagem
            
        #armazenando dados do aluno dentro do dicionario aluno
        aluno = {
            'matricula': matricula,
            'nome': nome,
            'faltas': faltas,
            'notas': notas,
            'média': media,
            'assiduidade': freq
        }

        dicionarioAlunos[nome] = aluno  #armazena os dados do aluno dentro do dicionário geral dos alunos

        disc = dicionarioTurma['nome disciplina']
        dicionarioCadastros[disc]['dado alunos'] = dicionarioAlunos

        j+=1
    #print(dicionarioCadastros)


#--- Função para média/desvio padrão da turma
def turmaMediaDesvio(dicionarioAlunos):
    medias = []  #lista para armazenar as médias de cada aluno
    for aluno in dicionarioAlunos:
        medias.append(dicionarioAlunos[aluno]['média'])

    mediaTurma = round(np.average(medias), 1)  #uso do numpy para calcular a média
    desvioTurma = round(np.std(medias), 1)  #uso do numpy para calcular desvio
    return mediaTurma, desvioTurma, medias  #retorn tupla com 3 listas


#--- Função para lista de aprovados/reprovados
def alunosAprovadosReprovados(dicionarioAlunos):
    #listas para armazenar nome dos alunos aprovados/reprovados
    aprovados = []  
    reprovados = []

    for aluno in dicionarioAlunos:
        if dicionarioAlunos[aluno]['média'] < 7 or dicionarioAlunos[aluno]['assiduidade'] < 75:  #aluno é considerado reprovado se média<7 e se assiduidade<75%
            reprovados.append(dicionarioAlunos[aluno]['nome'])
        elif dicionarioAlunos[aluno]['média'] >= 7:
            aprovados.append(dicionarioAlunos[aluno]['nome'])
    
    return aprovados, reprovados  #retorna tupla com 2 listas


#--- menu de acesso aos dados da turma
def menuAcessoTurma(dicionarioTurma):
    print(f'''
    * * * * * * * * * * * * *{dicionarioTurma['nome disciplina']}* * * * * * * * * * *
    *    - Cadastrar aluno;                                      (1)*
    *    - Acessar dados da Turma;                               (2)*
    *    - Acessar dados de um Aluno;                            (3)*
    *    - Média da turma;                                       (4)*
    *    - Desvio padrão da turma;                               (5)*
    *    - Lista com nome dos alunos aprovados;                  (6)*
    *    - Lista com nome dos alunos reprovados;                 (7)*
    *    - Gerar gráficos sobre rendimento da turma;             (8)*
    *    - Gerar arquivo com dados da turma;                     (9)*
    *    - Acessar informações sobre a disciplina;              (10)*
    *    - Voltar ao menu principal;                             (0)*
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    ''')


#--- Programa principal
dicionarioCadastros = {}
dicionarioTurma = {}
dicionarioAlunos = {}

while True:
    menu()
    opcao = int(input('Digite sua opção: '))

    #--- Opção de cadastrar nova turma
    if opcao == 1:
        cadastroTurma(dicionarioTurma, dicionarioCadastros)

        while True:
            menuAcessoTurma(dicionarioTurma)
            opcaoTurma = int(input('*   - Digite sua opção: '))

            if opcaoTurma == 1:
                cadastroaluno(dicionarioAlunos, dicionarioTurma, dicionarioCadastros)
            elif opcaoTurma == 2:
                print(pd.DataFrame.from_dict(dicionarioAlunos))  #é criado dataframe para imprimir as informações em tabela
            elif opcaoTurma == 3:
                aluno = input('Digite nome do aluno: ')
                print(dicionarioAlunos[aluno])
            elif opcaoTurma == 4:
                print('A média da turma é ', turmaMediaDesvio(dicionarioAlunos)[0])
            elif opcaoTurma == 5:
                print('O desvio padrão da turma é ', turmaMediaDesvio(dicionarioAlunos)[1])
            elif opcaoTurma == 6:
                aprovados = str(alunosAprovadosReprovados(dicionarioAlunos)[0])
                print('Os alunos aprovados foram: ', aprovados[1:-1])
            elif opcaoTurma == 7:
                reprovados = str(alunosAprovadosReprovados(dicionarioAlunos)[1])
                print('Os alunos reprovados foram: ', reprovados[1:-1])
            elif opcaoTurma == 8:
                print('''
                Escolha opção de gráfico:
                [1] Gráfico de aprovações
                [2] Gráfico de médias
                [3] Gráfico de assiduidade
                ''')
                opcaoGraf = int(input('opção de gráfico: '))

                if opcaoGraf == 1:
                    aprov = alunosAprovadosReprovados(dicionarioAlunos)[0]
                    reprov = alunosAprovadosReprovados(dicionarioAlunos)[1]

                    labels = 'Aprovados', 'Reprovados'
                    sizes = [len(aprov), len(reprov)]

                    fig1, ax1 = plt.subplots()
                    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
                    ax1.axis('equal')  #gráfico em círculo
                    plt.title('Gráfico de aprovações')
                    plt.show()
                
                elif opcaoGraf == 2:
                    medias = turmaMediaDesvio(dicionarioAlunos)[2]
                    plt.hist(medias)  #histograma das médias
                    plt.title('Gráfico de médias')
                    plt.show()

                elif opcaoGraf == 3:
                    freq = []  #lista para armazenar a frequência de cada aluno
                    for aluno in dicionarioAlunos:
                        freq.append(dicionarioAlunos[aluno]['assiduidade'])

                    plt.hist(freq)
                    plt.title('Gráfico de assiduidade')
                    plt.show()

            elif opcaoTurma == 9:
                with open('arquivoTurma.txt', 'w') as file:
                    dado = pd.DataFrame.from_dict(dicionarioAlunos)  #cria dataframe com os dados
                    dadoStr = dado.to_string()  #converte tipo do dataframe em string
                    file.write(dadoStr)  #salva o dado em formato de tabela
            elif opcaoTurma == 10:
                print(dicionarioTurma)
            elif opcaoTurma == 0:
                break
            else:
                print('ERRO. Digite novamente sua opção.')

        clear()

    #--- Opção de acessar turma já cadastrada
    elif opcao == 2:
        if dicionarioCadastros == {}:
            print('Nenhuma turma foi cadastrada ainda.')
        else:
            nomeDis = input('    *  - Digite o nome da disciplina que você deseja acessar: ')
            if nomeDis not in dicionarioCadastros:
                print('ERRO. Não foi encontrada disciplina cadastrada com esse nome, digite novamente.')
                nomeDis = input('    *  - Digite o nome da disciplina que você deseja acessar: ')

            dicionarioTurma = dicionarioCadastros[nomeDis]['dado turma']
            dicionarioAlunos = dicionarioCadastros[nomeDis]['dado alunos']

            while True:
                menuAcessoTurma(dicionarioTurma)
                opcaoTurma = int(input('*   - Digite sua opção: '))

                if opcaoTurma == 1:
                    cadastroaluno(dicionarioAlunos, dicionarioTurma, dicionarioCadastros)
                elif opcaoTurma == 2:
                    print(pd.DataFrame.from_dict(dicionarioAlunos))  #é criado dataframe para imprimir as informações em tabela
                elif opcaoTurma == 3:
                    aluno = input('Digite nome do aluno: ')
                    print(dicionarioAlunos[aluno])
                elif opcaoTurma == 4:
                    print('A média da turma é ', turmaMediaDesvio(dicionarioAlunos)[0])
                elif opcaoTurma == 5:
                    print('O desvio padrão da turma é ', turmaMediaDesvio(dicionarioAlunos)[1])
                elif opcaoTurma == 6:
                    aprovados = str(alunosAprovadosReprovados(dicionarioAlunos)[0])
                    print('Os alunos aprovados foram: ', aprovados[1:-1])
                elif opcaoTurma == 7:
                    reprovados = str(alunosAprovadosReprovados(dicionarioAlunos)[1])
                    print('Os alunos reprovados foram: ', reprovados[1:-1])
                elif opcaoTurma == 8:
                    print('''
                    Escolha opção de gráfico:
                    [1] Gráfico de aprovações
                    [2] Gráfico de médias
                    [3] Gráfico de assiduidade
                    ''')
                    opcaoGraf = int(input('opção de gráfico: '))

                    if opcaoGraf == 1:
                        aprov = alunosAprovadosReprovados(dicionarioAlunos)[0]
                        reprov = alunosAprovadosReprovados(dicionarioAlunos)[1]

                        labels = 'Aprovados', 'Reprovados'
                        sizes = [len(aprov), len(reprov)]

                        fig1, ax1 = plt.subplots()
                        ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
                        ax1.axis('equal')  #gráfico em círculo
                        plt.title('Gráfico de aprovações')
                        plt.show()
                    
                    elif opcaoGraf == 2:
                        medias = turmaMediaDesvio(dicionarioAlunos)[2]
                        plt.hist(medias)  #histograma das médias
                        plt.title('Gráfico de médias')
                        plt.show()

                    elif opcaoGraf == 3:
                        freq = []  #lista para armazenar a frequência de cada aluno
                        for aluno in dicionarioAlunos:
                            freq.append(dicionarioAlunos[aluno]['assiduidade'])

                        plt.hist(freq)
                        plt.title('Gráfico de assiduidade')
                        plt.show()

                elif opcaoTurma == 9:
                    with open('arquivoTurma.txt', 'w') as file:
                        dado = pd.DataFrame.from_dict(dicionarioAlunos)  #cria dataframe com os dados
                        dadoStr = dado.to_string()  #converte tipo do dataframe em string
                        file.write(dadoStr)  #salva o dado em formato de tabela
                elif opcaoTurma == 10:
                    print(dicionarioTurma)
                elif opcaoTurma == 0:
                    break
                else:
                    print('ERRO. Digite novamente sua opção.')

    elif opcao == 0:
        break
    else:
                print('ERRO. Digite novamente sua opção.')


