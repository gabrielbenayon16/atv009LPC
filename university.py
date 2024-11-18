from department import Department

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
        else:
            print(f"The department '{department.name}' is already linked to the university.")

    def remove_department(self, department):
        if department in self.departments:
            department.remove_all_professors()
            self.departments.remove(department)
        else:
            print(f"The department '{department.name}' is not in this university.")

    def remove_all_departments(self):
        for department in list(self.departments):
            self.remove_department(department)

    def list_departments(self):
        return [dep.name for dep in self.departments]
