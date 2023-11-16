# databasetest2.py

import sqlite3

#연결객체 리턴
con=sqlite3.connect("c:\\work\\sample.db")

cur=con.cursor()

#테이블구조
cur.execute("create table phonebook (name text, phoneNum text);")

# 1건입력
cur.execute("insert into Phonebook values ('홍길동','010-222');")

# 입력파라메터
name = "전우치"
phoneNumber = "010-123"
cur.execute("insert into Phonebook values (?,?);",(name,phoneNumber))

# n건입력
datalist=(('박문수','010-333'),('김길동','010-567'),('김길동','010-666'),('김길동','010-555'))
cur.executemany("insert into Phonebook values (?,?);",datalist)

# 검색
cur.execute("select * from phonebook;")
print(cur.fetchall())

#작업완료
con.commit()