hour1 = int(input('hour1 '))
min1 = int(input('min1 '))
sec1 = int(input('sec1 '))
hour2 = int(input('hour2'))
min2 = int(input('min2'))
sec2 = int(input('sec2'))


time1 = hour1*3600
time2 = min1*60
time3 = time1 + time2 + sec1

time4 = hour2*3600
time5 = min2*60
time6 = time4 + time5 + sec2

print(time6 - time3)




























