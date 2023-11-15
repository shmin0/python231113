Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
dir(time)
['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']
time.time
<built-in function time>
time.time()
1700025315.982489
time.time()
1700025327.2745492
time.gmtime
<built-in function gmtime>
time.gmtime()
time.struct_time(tm_year=2023, tm_mon=11, tm_mday=15, tm_hour=5, tm_min=15, tm_sec=50, tm_wday=2, tm_yday=319, tm_isdst=0)
time.localtime()
time.struct_time(tm_year=2023, tm_mon=11, tm_mday=15, tm_hour=14, tm_min=15, tm_sec=59, tm_wday=2, tm_yday=319, tm_isdst=0)

time.sleep(10)
time.sleep(3)
from datetime import *
from datetime import *
dir()
['MAXYEAR', 'MINYEAR', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'time', 'timedelta', 'timezone', 'tzinfo']

d1=date(2023,12,5)
d1
datetime.date(2023, 12, 5)
d2=date.today()
d2
datetime.date(2023, 11, 15)
d3=datetime.now()
d3
datetime.datetime(2023, 11, 15, 14, 19, 36, 203314)
add=timedelta(days=100)
d2+add
datetime.date(2024, 2, 23)
datetime.date(2024, 2, 23)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    datetime.date(2024, 2, 23)
TypeError: descriptor 'date' for 'datetime.datetime' objects doesn't apply to a 'int' object






























d11=date(2019,05,27)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
d11=date(2019,5,27)
d2+add
datetime.date(2024, 2, 23)
>>> d11+add
datetime.date(2019, 9, 4)
>>> 
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.random()
0.3034635333033251
>>> random.uniform(1.0,5.0)
1.3544132379628477
>>> [random.randrange(20) for i in range(10)]
[16, 0, 17, 10, 13, 1, 8, 8, 14, 2]
>>> random.sample(range(20),10)
[16, 10, 7, 14, 2, 9, 4, 6, 1, 8]
>>> random.sample(range(45),7)
[9, 2, 17, 31, 27, 32, 23]
>>> 
>>> random.sample(range(45),7)
[38, 27, 40, 16, 34, 43, 44]
>>> 
>>> lotto=list(range(1,46))
>>> lotto
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> random.shuffle(lotto)
>>> lotto
[17, 8, 44, 4, 21, 34, 37, 28, 3, 18, 24, 20, 30, 19, 13, 12, 43, 5, 2, 16, 38, 27, 26, 33, 25, 32, 39, 23, 15, 29, 11, 40, 22, 41, 7, 45, 42, 9, 10, 1, 14, 36, 31, 6, 35]
