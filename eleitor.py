from datetime import datetime


class Eleitor():

    def __init__(self, nome: str, mae: str, pai: str, data_nasc: str, titulo: str, votou: str, zona: str, secao: str, municipio: str, uf: str, data_insc: str) -> None:
        self.nome = nome
        self.mae, = mae
        self.pai, = pai
        self.data_nasc = data_nasc
        self.titulo = titulo
        self.zona = zona
        self.secao = secao
        self.municipio = municipio
        self.uf = uf
        self.data_insc = data_insc
        self.votou = votou

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
        nasc = self.data_nasc[::-4]
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
