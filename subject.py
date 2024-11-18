class Subject:
    def __init__(self, name, workload, professor=None):
        self.name = name
        self.workload = workload
        self.professor = professor

    def subject_info(self):
        return {
            "name": self.name,
            "workload": self.workload,
            "professor": self.professor.name if self.professor else "None"
        }
