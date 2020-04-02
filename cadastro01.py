from interface import *
from arquivo import *
from time import sleep
arq = 'CadastroAJN.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])
    if resposta == 1:
        #Opção para ler um arquivo e ver os alunos cadastrados
        cabecalho('\033[33mALUNOS REGISTRADOS\033[m'.center(40))
        try:
            lerArquivo(arq)
        except:
            print('\033[31mERRO AO LER OS DADOS DO ARQUIVO!!\033[m')
    elif resposta == 2:
        cabecalho('NOVO CADASTRO'.center(40))
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        turma = str(input('Qual turma o aluno pertence? ')).strip().capitalize()
        escreverArquivo(arq, nome, idade, turma)

    elif resposta == 3:
        sleep(1)
        print('sair do programa.')
        break
    else:
        print(f'\033[31mA OPÇÃO {resposta} É INVALIDA, INSIRA UM VALOR VALIDO.\033[m')
