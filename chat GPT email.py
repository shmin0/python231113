import re

# 이메일 주소를 검증하는 정규표현식
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 이메일 주소를 포함한 텍스트 샘플
emails = [
    'example@example.com',
    'user@email.co.uk',
    'invalid_email@com',
    'anotherexample.com',
    'test.email@example.co.jp',
    'email_123@test-mail.com',
    'user@domain-with-dash.com',
    'email@sub.domain.com',
    'email@123.123.123.123',
    'email@[123.123.123.123]'
]

# 각 이메일 주소를 검증하고 결과 출력
for email in emails:
    if re.search(email_pattern, email):
        print(f"{email}: 유효한 이메일 주소")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소")
