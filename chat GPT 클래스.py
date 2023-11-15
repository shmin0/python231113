# chat GPT 클래스 

class Person:
    def __init__(self, person_id, title):
        self.id = person_id
        self.title = title

    def printinfo(self):
        print(f"ID: {self.id}, Title: {self.title}")

class Manager(Person):
    def __init__(self, person_id, title, skill):
        super().__init__(person_id, title)
        self.skill = skill

    def printinfo(self):
        super().printinfo()
        print(f"Skill: {self.skill}")

class Employee(Person):
    def __init__(self, person_id, title, role):
        super().__init__(person_id, title)
        self.role = role

    def printinfo(self):
        super().printinfo()
        print(f"Role: {self.role}")

# 샘플 코드
manager1 = Manager(1, "Manager", "Leadership")
manager1.printinfo()

employee1 = Employee(2, "Employee", "Developer")
employee1.printinfo()

# 추가적인 테스트 코드
manager2 = Manager(3, "Senior Manager", "Communication")
manager2.printinfo()

employee2 = Employee(4, "Intern", "Trainee")
employee2.printinfo()

manager3 = Manager(5, "Project Manager", "Project Management")
manager3.printinfo()

employee3 = Employee(6, "Senior Developer", "Senior Developer")
employee3.printinfo()

manager4 = Manager(7, "HR Manager", "HR Management")
manager4.printinfo()

employee4 = Employee(8, "Marketing Specialist", "Marketing")
employee4.printinfo()

manager5 = Manager(9, "Technical Manager", "Technical Skills")
manager5.printinfo()

employee5 = Employee(10, "Designer", "Design")
employee5.printinfo()