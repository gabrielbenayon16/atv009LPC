from universidade import Universidade
from departamento import Departamento
from professor import Professor
from disciplina import Disciplina


def main():

    universidade = Universidade("UEA")
    print(f"\nUniversidade: {universidade.nome}")

    # criando departamentos e professores
    departamentos_nomes = [
        "Departamento de Computação",
        "Departamento de Ciclo Básico",
        "Departamento de Mecânica",
        "Departamento de Elétrica",
        "Departamento de Química",
    ]
    professores_nomes = [
        "Ciclano da Silva",
        "Beltrano de Souza",
        "Raimundo Nonato",
        "Girafales",
        "Brás Cubas",
    ]

    departamentos = [
        Departamento(nome) for nome in departamentos_nomes
    ]
    professores = [
        Professor(nome) for nome in professores_nomes
    ]

    for dep, prof in zip(departamentos, professores):
        universidade.adicionar_departamento(dep)
        dep.adicionar_professor(prof)

    print("\nDepartamentos:")
    for departamento in universidade.listar_departamentos():
        print(f"- {departamento}")

    print("\nProfessores adicionados:")
    for dep in departamentos:
        print(f"{dep.nome}: {dep.listar_professores()}")

    # criando disciplinas
    disciplinas_dados = [
        ('Programação de Computadores e Algoritmos', 60),
        ("Cálculo 1", 90),
        ("Mecânica dos Sólidos", 66),
        ("Eletricidade", 66),
        ('Química Geral', 60),
    ]

    disciplinas = [
        Disciplina(nome, carga_horaria, prof)
        for (nome, carga_horaria), prof in zip(disciplinas_dados, professores)
    ]

    for prof, disc in zip(professores, disciplinas):
        prof.adicionar_disciplina(disc)

    print("\nDisciplinas adicionadas:")
    for prof in professores:
        print(f"{prof.nome}: {prof.listar_disciplinas()}")

    print("\nDetalhes das Disciplinas:")
    for disc in disciplinas:
        print(f"- {disc.informacoes_disciplina()}")


# executar o programa
if __name__ == "__main__":
    main()
