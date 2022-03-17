from eleitor import Eleitor


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

    def imprimir(self, nome, titulo):
        eleitor = self.buscar(nome, titulo)

        if eleitor:
            eleitor = eleitor.get_info()
            print(f'Eleitor(a): {eleitor[0]}\nMãe: {eleitor[1]}\nPai: {eleitor[2]}\nData de nascimento: {eleitor[3]}\nTitulo: {eleitor[4]}\nZona: {eleitor[5]}  Seção: {eleitor[6]}\nMunicipio: {eleitor[7]}  UF: {eleitor[8]}\n\n')
        else:
            print('Eleitor Não Cadastrado!')
