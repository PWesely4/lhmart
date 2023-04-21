import sys
import math
import string

v = []

x = []

a = []

def get_data():
  global v, x, a

  case_count = int(sys.stdin.readline().rstrip())

  for num in range(case_count):
    case = (sys.stdin.readline().rstrip())
    a.append(case)

  for num in range(case_count):
    strvar = a[num]
    strvar = str(strvar)
    temp = 0
    sort = ''
    run = 0
    while run == 0:
      if strvar[temp] != ':':
        sort += strvar[temp]
        temp += 1  
      else:
        v.append(float(sort))
        sort = ''
        temp += 1
        run = 1
    while run == 1:
      if temp >= len(strvar):
        x.append(float(sort))
        sort = ''
        run  = 2
      else:
        sort += strvar[temp]
        temp += 1

def check_output():
  global v, x
  for temp in range(len(v)):
    speed = v[temp]
    distance = x[temp]
    if speed >= distance:
      print('SWERVE')
    elif: