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
        self.set_info()
        self.set_idade()
        self.set_situacao()

        pass

    def set_info(self):
        self.info = [self.nome, self.mae, self.pai, self.data_nasc, self.titulo, self.zona,
                     self.secao, self.municipio, self.uf, self.data_insc, self.votou]
        pass

    def get_info(self):
        return self.info

    def set_idade(self):
        ano_nasc = int(self.data_nasc[-4::])
        mes_nasc = int(self.data_nasc[3:5])
        dia_nasc = int(self.data_nasc[0:2])
        ano_atual = int(datetime.now().strftime('%Y'))
        mes_atual = int(datetime.now().strftime('%m'))
        dia_atual = int(datetime.now().strftime('%d'))

        idade = ano_atual - ano_nasc
        if mes_nasc == 2 and dia_nasc == 29:
            dia_nasc = dia_nasc - 1
        if mes_atual < mes_nasc:
            idade = idade - 1
        elif mes_atual == mes_nasc:
            if dia_atual < dia_nasc:
                idade = idade - 1

        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_situacao(self):
        idade = self.get_idade()
        votou = self.get_info()[-1]
        obrigatorio = True if (idade >= 18 and idade < 70) else False
        situacao = 'Irregular' if (
            votou == '0' and obrigatorio == True) else 'Regular'
        self.situacao = situacao
        pass

    def get_situacao(self):
        return self.situacao
