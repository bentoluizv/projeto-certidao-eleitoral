from main import *

eleitores = obter_eleitores()

print('Digite:\n1 - Cadastrar novo eleitor\n2 - Emitir certidão de quitação eleitoral\n')
option = int(input())

if option not in [1, 2]:
    print('Opção Incorreta')
elif option == 1:
    eleitor = obter_dados()
    if not buscar(eleitor[0], eleitor[4], eleitores):
        cadastrar(eleitor)
    else:
        print('Eleitor já cadastrado!')
else:
    eleitor = input('Digite seu nome completo: ')
    titulo = input('Digite seu número de inscrição do titulo eleitoral: ')
    if buscar(eleitor, titulo, eleitores):
        print('Emitir certidão')
    else:
        print('Eleitor não cadastrado.')
