class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        if len(self.departamentos) < 5:
            self.departamentos.append(departamento)
        else:
            print("A universidade já atingiu o limite de 5 departamentos.")

    def listar_departamentos(self):
        return [d.nome for d in self.departamentos]
