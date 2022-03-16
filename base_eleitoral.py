class Base():
    def __init__(self) -> None:
        self.eleitores = []
        self.set_data()
        pass

    def set_data(self):
        base = open('data\eleitores.csv', 'r', encoding='utf8')
        data = base.readlines()
        base.close()
        self.eleitores = [eleitor.strip().split(';') for eleitor in data]
        pass

    def get_data(self):
        return self.eleitores

    def buscar(self, nome: str, titulo: str):
        eleitores = self.get_data()
        eleitor = []

        for el in eleitores:
            if el[0] == nome and el[4] == titulo:
                eleitor = el

        return eleitor

    def imprimir(self):
        eleitor = self.buscar()
        if eleitor:
            print(f'Eleitor(a): {eleitor[0]}\nMãe: {eleitor[1]}\nPai: {eleitor[2]}\nData de nascimento: {eleitor[3]}\nTitulo: {eleitor[4]}\nZona: {eleitor[5]}  Seção: {eleitor[6]}\nMunicipio: {eleitor[7]}  UF: {eleitor[8]}\n\n')
        else:
            print('Eleitor Não Cadastrado!!')
        pass
