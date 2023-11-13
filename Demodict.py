# Demodict.py

device={'아이폰':5,'아이패드':10,'윈도우타블렛':20}

print(len(device))
print(device)

print(device['아이폰'])
device['맥북']=15

del device['아이패드']
print(device)

device['아이폰']=6

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

