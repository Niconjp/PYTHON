# https://www.codewars.com/kata/52685f7382004e774f0001f7/python

# 5 kyu

# Human Readable Time

def make_readable(s):
    min, sec = divmod(s, 60)
    hour, min = divmod(min, 60)
    return "%02d:%02d:%02d" % (hour, min, sec)
