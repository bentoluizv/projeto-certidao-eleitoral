from datetime import datetime


class Eleitor():
    nome = ''
    titulo = ''
    data_nasc = ''
    mae = ''
    pai = ''
    zona = ''
    secao = ''
    municipio = ''
    uf = ''
    data_insc = ''
    votou = ''

    def __init__(self, nome: str, titulo: str, data_nasc: str) -> None:
        self.nome = nome
        self.titulo = titulo
        self.data_nasc = data_nasc

        self.set_info()
        self.set_idade()
        pass

    def set_data(self):
        self.mae, = input('Mãe: ')
        self.pai, = input('Pai: ')
        self.zona = input('Zona Eleitoral: ')
        self.secao = input('Seção Eleitoral: ')
        self.municipio = input('Municipio: ')
        self.uf = input('UF: ')
        self.data_insc = ('Data de Emissão do Titulo de Eleitor: ')
        self.votou = ('Votou na ultima eleição: \n  1 - SIM\n  0 - NÃO\n\n')
        pass

    def set_info(self) -> None:

        self.info = [self.nome, self.mae, self.pai, self.data_nasc, self.titulo,
                     self.zona, self.secao, self.municipio, self.uf, self. data_insc, self.votou]
        pass

    def get_info(self):
        return self.info

    def set_idade(self):
        nasc = self.data_nasc[-4::]
        ano_atual = datetime.now().strftime('%Y')
        self.idade = int(ano_atual) - int(nasc)
        pass

    def get_idade(self):
        return self.idade

    def voto_obrigatorio(self):
        idade = self.get_idade()
        if idade >= 18 and idade < 70:
            return True
        return False
