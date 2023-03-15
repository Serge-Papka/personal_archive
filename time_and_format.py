'''
Задание:
только время;
только минуты;
только дату;
только месяц.
'''
import time

# seconds = time.time() # текущее время в сек
# time_now = time.ctime(seconds) # строчка текущей даты
# print(type(time_now),time_now)
# time.sleep(1)
# print(time.struct_time.tm_year) # <class 'str'> Wed Mar 15 12:57:28 2023
'''
0	tm_year	0000, …, 2019, …, 9999
1	tm_mon	1, 2, …, 12
2	tm_mday	1, 2, …, 31
3	tm_hour	0, 1, …, 23
4	tm_min	0, 1, …, 59
5	tm_sec	0, 1, …, 61
6	tm_wday	0, 1, …, 6; Monday is 0
7	tm_yday	1, 2, …, 366
8	tm_isdst	0, 1 or -1
'''

result = time.localtime(time.time())
# print("результат:", result)
# print("\nгод:", result.tm_year)
# print("tm_hour:", result.tm_hour)
# print(type(result)) # <class 'time.struct_time'>
print(f'{result.tm_hour:02}:{result.tm_min:02}:{result.tm_sec:02} ')
print(f'{result.tm_min:02}')
print(f'{result.tm_mday:02}.{result.tm_mon:02}:{result.tm_year} ')
print(f'{result.tm_mon:02}')