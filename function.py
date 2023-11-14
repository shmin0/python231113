def setvalue(newValue):
    x=newValue
    print('지역변수:',x)


retvalue=setvalue(5)
print(retvalue)

def swap(x,y):
    return y,x

print(swap(3,4))

print('---지역변수와 전역변수---')
x=5
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=1
    return a+x

print(func2(1))
print(globals())
print(dir())


#기본값이 있는 함수
def times(a=10, b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))

#키워드 인자 

def connectURL(server, port):
    strURL="http://"+ server+":"+port
    return strURL

print(connectURL('multi.com','80'))
print(connectURL(port='8080', server='multi.com'))

#가변인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union('ham','egg'))
print(union('ham','egg','spam'))

g=lambda x,y : x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print((lambda x,y:x*y)(3,4))
print(globals())
