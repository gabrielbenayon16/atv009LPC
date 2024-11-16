from universidade import Universidade
from departamento import Departamento


def main():

    # criando a universidade
    universidade = Universidade("UEA")
    print(f"\nUniversidade: {universidade.nome}")

    # criando departamentos
    departamento1 = Departamento("Departamento de Ciclo Básico")
    departamento2 = Departamento("Departamento de Computação")
    departamento3 = Departamento("Departamento de Elétrica")
    departamento4 = Departamento("Departamento de Mecânica")
    departamento5 = Departamento("Departamento de Química")
    universidade.adicionar_departamento(departamento1)
    universidade.adicionar_departamento(departamento2)
    universidade.adicionar_departamento(departamento3)
    universidade.adicionar_departamento(departamento4)
    universidade.adicionar_departamento(departamento5)
    print("\nDepartamentos:")
    for departamento in universidade.listar_departamentos():
        print(f"- {departamento}")


# executar o programa
if __name__ == "__main__":
    main()
