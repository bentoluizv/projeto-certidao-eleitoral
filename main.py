def obter_eleitores():
    base = open('data\eleitores.csv', 'r', encoding='utf8')
    eleitores = base.readlines()
    base.close()
    eleitores = [eleitor.strip().split(';') for eleitor in eleitores]
    return eleitores


def obter_dados():
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
    dados = [nome, mae, pai, data_nasc, titulo,
             zona, secao, municipio, uf, data_insc, votou]
    return dados


def cadastrar(dados: list):
    eleitor = ';'.join(dados)
    base = open('data\eleitores.csv', 'a')
    base.write('\n' + eleitor)
    base.close()


def buscar(nome: str, titulo: str, eleitores: list):
    for eleitor in eleitores:
        if (eleitor[0] == nome) and (eleitor[4] == titulo):
            print(f'Eleitor(a): {eleitor[0]}\nMãe: {eleitor[1]}\nPai: {eleitor[2]}\nData de nascimento: {eleitor[3]}\nTitulo: {eleitor[4]}\nZona: {eleitor[5]}  Seção: {eleitor[6]}\nMunicipio: {eleitor[7]}  UF: {eleitor[8]}\n\n')
            return True
    return False


# TODO def emitir_certidao():
