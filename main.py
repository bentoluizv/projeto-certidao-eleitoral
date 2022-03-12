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


def cadastrar(dados):
    eleitor = ';'.join(dados)
    base = open('data\eleitores.csv', 'a')
    base.write('\n' + eleitor)
    base.close()
