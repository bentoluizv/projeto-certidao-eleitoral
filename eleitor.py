from datetime import datetime


class Eleitor():
    nome = ''
    mae = ''
    pai = ''
    data_nasc = ''
    titulo = ''
    zona = ''
    secao = ''
    municipio = ''
    uf = ''
    data_insc = ''
    votou = ''
    idade = ''
    situacao = ''
    info = []

    def __init__(self, dados: list[str]) -> None:
        [self.nome, self.mae, self.pai, self.data_nasc, self.titulo, self.zona,
            self.secao, self.municipio, self.uf, self.data_insc, self.votou] = dados
        self.set_idade()
        self.set_info()

        pass

    def set_idade(self):
        nasc = self.data_nasc[-4::]
        ano_atual = datetime.now().strftime('%Y')
        self.idade = int(ano_atual) - int(nasc)
        pass

    def get_idade(self):
        return self.idade

    def set_info(self):
        self.info = [self.nome, self.mae, self.pai, self.data_nasc, self.titulo, self.zona,
                     self.secao, self.municipio, self.uf, self.data_insc, self.votou]
        pass

    def get_info(self):
        return self.info

    def set_situacao(self):
        pass

    def get_situacao(self):
        pass
