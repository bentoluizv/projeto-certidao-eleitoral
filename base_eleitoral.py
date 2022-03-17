from eleitor import Eleitor
from datetime import datetime
from os import path, mkdir


class Base():
    data = []

    def __init__(self) -> None:
        self.set_data()
        pass

    def set_data(self):
        base = open('data\eleitores.csv', 'r', encoding='utf8')
        data = base.readlines()
        base.close()
        self.data = [eleitor.strip().split(';') for eleitor in data]
        pass

    def get_data(self):
        return self.data

    def buscar(self, nome: str, titulo: str):
        eleitores = self.get_data()
        eleitor = []
        for el in eleitores:
            if el[0] == nome and el[4] == titulo:
                eleitor = Eleitor(el)
        return eleitor

    def imprimir(self, nome: str, titulo: str):
        eleitor = self.buscar(nome, titulo)
        conteudo = f'\nEleitor(a): {eleitor.nome}\nMãe: {eleitor.mae}\nPai: {eleitor.pai}\nData de nascimento: {eleitor.data_nasc}\nTitulo: {eleitor.titulo}\nZona: {eleitor.zona}  Seção: {eleitor.secao}\nMunicipio: {eleitor.municipio}  UF: {eleitor.uf}\nIdade: {eleitor.idade} anos\nSituação Eleitoral: {eleitor.situacao}\n'
        if eleitor:
            return conteudo
        else:
            return ''

    def emitir_certidao(self, nome: str, titulo: str):
        base = open('certidao_modelo.html', 'r')
        modelo = base.read()
        base.close()
        eleitor = self.buscar(nome, titulo)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        hora_atual = datetime.now().strftime("%H:%M:%S")

        if eleitor.situacao == 'Regular':
            modelo = modelo.replace('$NOME$', f'{eleitor.nome}')
            modelo = modelo.replace('$TITULO$', f'{eleitor.titulo}')
            modelo = modelo.replace(' $CIDADE$', f'{eleitor.municipio}')
            modelo = modelo.replace('$NASC$', f'{eleitor.data_nasc}')
            modelo = modelo.replace('$MAE$', f'{eleitor.mae}')
            modelo = modelo.replace('$PAI$', f'{eleitor.pai}')
            modelo = modelo.replace('$ZONA$', f'{eleitor.zona}')
            modelo = modelo.replace('$SEC$', f'{eleitor.secao}')
            modelo = modelo.replace('$UF$', f'{eleitor.uf}')
            modelo = modelo.replace('$DATA_DOMILICIO$', f'{eleitor.data_insc}')
            modelo = modelo.replace('$HORA$', f'{hora_atual}')
            modelo = modelo.replace('$DATA$', f'{data_atual}')
        else:
            return False

        if not path.exists('certidoes_emitidas'):
            mkdir('certidoes_emitidas')

        caminho = f'certidoes_emitidas\certidao_{titulo.strip()}.html'
        certidao = open(caminho, 'w')
        certidao.write(modelo)
        certidao.close()

        return True
