
import sys

one=int(sys.argv[1])
two=int(sys.argv[2])
three=str(sys.argv[3])

def part1():
    if (one < two):
        print(two)
    elif (one == two):
        #equal
        pass
    else:
        print(one)

def part2():
    if three.find('time') >= 0:
        print(one+two)

def part3():
    if (one % 2 == 1 and two % 2 == 1):
        print(three)
    elif (one % 3 == 0 or two % 3 == 0):
        print(three)

def part4():
    if len(sys.argv)>4:
        print('error')

def all_in_one():
    part1()
    part2()
    part3()
    part4()

all_in_one()
