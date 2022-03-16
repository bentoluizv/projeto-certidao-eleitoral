from datetime import datetime


class Eleitor:

    def __init__(self) -> None:
        self.nome = input('Nome: ')
        self.mae, = input('Mãe: ')
        self.pai, = input('Pai: ')
        self.data_nasc = input('Data de Nascimento: ')
        self.titulo = input('Titulo Eleitoral: ')
        self.zona = input('Zona: ')
        self.secao = input('Seção: ')
        self.municipio = input('Municipio: ')
        self.uf = input('UF: ')
        self.data_insc = input('Data de Emissão do Titulo de Eleitor: ')
        self.votou = input('Votou na ultima eleição?\n 1 - SIM\n 0 - NÃO: ')
        self.set_info()
        self.set_idade()
        pass

    def set_info(self) -> None:
        self.info = [self.nome, self.mae, self.pai, self.data_nasc, self.titulo,
                     self.zona, self.secao, self.municipio, self.uf, self. data_insc, self.votou]
        pass

    def get_info(self):
        return self.info

    def set_idade(self):
        nasc = self.data_nasc
        ano_atual = datetime.now().strftime('%Y')
        self.idade = int(ano_atual) - int(nasc)
        pass

    def get_idade(self):
        return self.idade

    def voto_obrigatorio(self):
        pass

    def set_situacao(self):
        pass
