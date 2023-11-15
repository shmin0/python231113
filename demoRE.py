#demoRE

#일반적인 검색
import re
result=re.search('[0-9]*th','  35th')
print(result)
print(result.group())

# 정확하게 일치
# result=re.match('[0-9]*th','  35th')
# print(result)
# print(result.group())

result=re.search('\d{4}','올해는 2023년')
print(result.group())

result=re.search('\d{5}','우리동네는 51200')
print(result.group())

