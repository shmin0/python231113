# class1.py
# 클래스 정의

class person:
    def __init__(self):
        self.name = 'default name'
    def print(self):
        print('My name is {0}'.format(self.name))

# 인스턴스 정의
p1=person()
p2=person()
p1.name='전우치'

# 메서드 호출
p1.print()
p2.print()

#런타임(코드 실행중)

person.title = 'new title'
print(p1.title)
print(p2.title)
print(person.title)