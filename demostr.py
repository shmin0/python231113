# demostr.py

strA='python is very powerful'
strB= '파이썬은 강력해'
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count('p'))
print(strA.startswith('py'))
print(strA.endswith('ful'))
print('--알파벳과 숫자로 구성---')
print('MBC2580'.isalnum())
print('MBC:2580'.isalnum())
print('2580'.isdecimal())
data='<<<spam and hum>>>'
result=data.strip("<>")
print(data)
print(result)
# result=result.replace('spam','spane gg')
# print('변환결과')
# print(result)
# lst=result.split()
# print(lst)
# print('---다시 합치기 ---')
# print(':)'.join(lst))

result='spam::egg::ham'
print('변환결과')
print(result)
lst=result.split('::')
print(lst)
print('---다시 합치기 ---')
print(':)'.join(lst))


# 반복문자열 생성

names=['전우치','이순신','박문수']
for name in names:
    print('안녕하세요 {0}님 초겨울입니다'.format(name))
    print('='*40)

                                                        