# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

M,D,Y = map(int,input().split())
DN = int(calendar.weekday(Y,M,D))
print(calendar.day_name[DN].upper())
