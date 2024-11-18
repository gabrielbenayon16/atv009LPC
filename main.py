from university import University
from department import Department
from professor import Professor
from subject import Subject


def main():
    university = University("UEA")
    print(f"\nUniversity: {university.name}")

    # creating departments and professors
    department_names = [
        "Departamento de Computação",
        "Departamento de Ciclo Básico",
        "Departamento de Mecânica",
        "Departamento de Elétrica",
        "Departamento de Química",
    ]
    professor_names = [
        "Ciclano da Silva",
        "Beltrano de Souza",
        "Raimundo Nonato",
        "Girafales",
        "Brás Cubas",
    ]

    departments = [Department(name) for name in department_names]
    professors = [Professor(name) for name in professor_names]

    for dep, prof in zip(departments, professors):
        university.add_department(dep)
        dep.add_professor(prof)

    print("\nDepartments:")
    for department in university.list_departments():
        print(f"- {department}")

    print("\nAdded Professors:")
    for dep in departments:
        print(f"{dep.name}: {dep.list_professors()}")

    # creating subjects
    subject_data = [
        ('Programação de Computadores e Algoritmos', 60),
        ("Cálculo 1", 90),
        ("Mecânica dos Sólidos", 66),
        ("Eletricidade", 66),
        ('Química Geral', 60),
    ]

    subjects = [
        Subject(name, workload, prof)
        for (name, workload), prof in zip(subject_data, professors)
    ]

    for prof, subj in zip(professors, subjects):
        prof.add_subject(subj)

    print("\nAdded Subjects:")
    for prof in professors:
        print(f"{prof.name}: {prof.list_subjects()}")

    print("\nSubject Details:")
    for subj in subjects:
        print(f"- {subj.subject_info()}")


# execute the program
if __name__ == "__main__":
    main()
