

import sys

argument=sys.argv[1]
number=int(argument)
end=range(1,(number+1))

def four():
    for i in end:
        if i%12 == 0:
            dozen=i/12
            print(str(dozen)+' dozen')
        elif i%4 == 0:
            print('square')
        elif i%3 == 0:
            print('triangle')
    print(sum(end))

four()
