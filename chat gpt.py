from openpyxl import Workbook
from random import randint, choice

# 엑셀 워크북 생성
workbook = Workbook()
sheet = workbook.active
sheet.title = 'Sales Data'

# 데이터 헤더 추가
headers = ['전자제품 ID', '이름', '가격', '수량']
sheet.append(headers)

# 전자제품 데이터 생성 및 저장
for _ in range(100):
    product_id = randint(1000, 9999)  # 임의의 전자제품 ID 생성
    product_name = f'제품_{product_id}'  # 간단한 이름 생성
    price = round(randint(10, 1000), 2)  # 임의의 가격 생성 (10에서 1000 사이)
    quantity = randint(1, 50)  # 임의의 수량 생성

    # 데이터를 행에 추가
    sheet.append([product_id, product_name, price, quantity])

# 파일 저장
workbook.save(filename='sales.xlsx')
print("파일이 생성되었습니다: sales.xlsx")