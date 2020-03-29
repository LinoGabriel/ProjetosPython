def arquivoExiste(nome):
    """
    Verificação de existencia de arquivo
    :param nome: nome do arquivo
    :return: (True) - Caso consiga criar um arquivo / (False) Caso ocorra erro na criação do arquivo.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """

    :param nome:Cria o arquivo cujo o nome foi estipulado na area "cadastro01.py"
    :return: sem valor
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[31mERRO AO CRIAR ARQUIVO!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO AO LER ARQUIVO!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15}{dado[1]} anos(Turma {dado[2]})'.replace('\n', ''))
    finally:
        a.close()


def escreverArquivo(arq, nome='', idade='0', turma=''):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mOCORREU UM ERRO NA HORA DE ABRIR O ARQUIVO!\033[m')
    else:
        try:
            a.write(f'{nome};{idade};{turma}\n')
        except:
            print('\033[31mHOUVE UM ERRO AO CADASTRAR UM ALUNO!\033[M')
        else:
            print(f'\033[32mO aluno {nome} foi adcionado com sucesso!\033[m')
            a.close()
