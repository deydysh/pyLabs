a = int(input())
sec = a % 60
minutes = a // 60 % 60
hours = a // 3600 % 24

print("{:02}:{:02}:{:02}".format(hours, minutes, sec))
