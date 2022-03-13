from datetime import datetime


def obter_eleitores():
    base = open('data\eleitores.csv', 'r', encoding='utf8')
    eleitores = base.readlines()
    base.close()
    eleitores = [eleitor.strip().split(';') for eleitor in eleitores]
    return eleitores


def obter_dados_eleitor():
    nome = input('Digite seu nome completo : ')
    mae = input('Digite o nome da sua mãe: ')
    pai = input('Digite o nome do seu pai: ')
    data_nasc = input('Digite sua data de nascimento: ')
    titulo = input('Digite seu título de eleitor: ')
    zona = input('Digite sua zona eleitoral: ')
    secao = input('Digite sua seção eleitoral: ')
    municipio = input('Digite o município em que você vota: ')
    uf = input('Digite seu estado: ')
    data_insc = input('Digita sua data de inscrição: ')
    votou = input('Você votou na última eleição:\n1 - SIM\n0 - NÃO\n')
    eleitor = [nome, mae, pai, data_nasc, titulo,
               zona, secao, municipio, uf, data_insc, votou]
    return eleitor


def cadastrar(eleitor: list):
    eleitor = ';'.join(eleitor)
    base = open('data\eleitores.csv', 'a')
    base.write('\n' + eleitor)
    base.close()


def buscar(nome: str, titulo: str, eleitores: list):
    for eleitor in eleitores:
        if (eleitor[0] == nome) and (eleitor[4] == titulo):
            return True
    return False


def imprimir(nome: str, titulo: str, eleitores: list):
    for eleitor in eleitores:
        if (eleitor[0] == nome) and (eleitor[4] == titulo):
            print(f'Eleitor(a): {eleitor[0]}\nMãe: {eleitor[1]}\nPai: {eleitor[2]}\nData de nascimento: {eleitor[3]}\nTitulo: {eleitor[4]}\nZona: {eleitor[5]}  Seção: {eleitor[6]}\nMunicipio: {eleitor[7]}  UF: {eleitor[8]}\n\n')


def emitir_certidao(nome: str, titulo: str, eleitores: list):
    for eleitor in eleitores:
        if (eleitor[0] == nome) and (eleitor[4] == titulo):
            if eleitor[-1] == 0:
                print('Situação Irregular, eleitor não votou na ultima eleição, por favor comparecer ao cartório eleitoral para regularização do titulo.')

            else:
                base = open('certidao_modelo.html', 'r')
                modelo = base.read()
                base.close()

                data_atual = datetime.now().strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")

                modelo = modelo.replace('$NOME$', f'{eleitor[0]}')
                modelo = modelo.replace('$TITULO$', f'{eleitor[4]}')
                modelo = modelo.replace(' $CIDADE$', f'{eleitor[7]}')
                modelo = modelo.replace('$NASC$', f'{eleitor[3]}')
                modelo = modelo.replace('$MAE$', f'{eleitor[1]}')
                modelo = modelo.replace('$PAI$', f'{eleitor[2]}')
                modelo = modelo.replace('$ZONA$', f'{eleitor[5]}')
                modelo = modelo.replace('$SEC$', f'{eleitor[6]}')
                modelo = modelo.replace('$UF$', f'{eleitor[8]}')
                modelo = modelo.replace('$DATA_DOMILICIO$', f'{eleitor[9]}')
                modelo = modelo.replace('$HORA$', f'{hora_atual}')
                modelo = modelo.replace('$DATA$', f'{data_atual}')

                certidao = open(
                    f'certidoes_emitidas\certidao_{titulo.strip()}.html', 'w')
                certidao.write(modelo)
                certidao.close()
