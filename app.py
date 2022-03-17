from base_eleitoral import Base


def app():
    base = Base()
    option = input(
        '\nDigite:\n 1 - Buscar Eleitor\n 2 - Emitir Certidao de Quitação Eleitoral\n 3 - Sair\n')

    if option not in ['1', '2', '3']:
        print('Opção Incorreta!!\n')

    if option == '1':
        nome = input('\nNome do Eleitor: \n')
        titulo = input('\nNumero do Titulo Eleitoral: \n')
        eleitor = base.imprimir(nome, titulo)

        if eleitor == '':
            print('\nUsuário Não Cadastrado! \n')
            app()
        else:
            print(eleitor)
            app()

    elif option == '2':
        nome = input('\nNome do Eleitor: \n')
        titulo = input('\nNumero do Titulo Eleitoral: \n')
        certidao = base.emitir_certidao(nome, titulo)

        if certidao == False:
            print('\nSituação do eleitor irregular, favor comparecer ao cartório eleitoral para regularização do titulo\n')
            app()
        else:
            print('\nCertidão Emitida com Sucesso!!\n')
            app()

    else:
        print('\nSaindo do Aplicativo...\n')


app()
