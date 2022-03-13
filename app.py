from main import *


def App():
    eleitores = obter_eleitores()
    option_1 = int(input(
        'Digite:\n1 - Buscar eleitor\n2 - Cadastrar novo eleitor\n3 - Emitir certidão de quitação eleitoral\n0 - Sair\n\n'))
    if option_1 not in [1, 2, 3, 0]:
        print('Opção Incorreta!')
        App()
    elif option_1 == 0:
        print('Fechando Aplicativo!')
        return
    else:
        if option_1 == 1:
            nome = input('Digite o nome completo: ')
            titulo = input('Digite o número do titulo: ')
            if buscar(nome, titulo, eleitores):
                imprimir(nome, titulo, eleitores)
                print('Retornando ao menu principal!')
                App()
            else:
                print('Eleitor não cadastrado!')
                App()

        elif option_1 == 2:
            eleitor = obter_dados_eleitor()
            cadastrar(eleitor)
            print('Eleitor cadastrado com Sucesso! Retornando ao menu principal.')
            App()

        elif option_1 == 3:
            nome = input('Digite o nome completo: ')
            titulo = input('Digite o número do titulo: ')
            if buscar(nome, titulo, eleitores):
                emitir_certidao(nome, titulo, eleitores)
                print('Certidão emitida com sucesso! retornando ao menu principal...')
                App()
            else:
                print('Eleitor não cadastrado!')
                App()


App()
