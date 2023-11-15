class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    
    def working(self):
        print('현재코딩중...')


class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        # print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        # print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))
        print("Info(Name:{0}, Phone Number: {1},학과:{2}, 학번: {3})".format(self.name, self.phoneNumber,self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201122")
# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
s.working()