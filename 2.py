

import sys

arg1=int(sys.argv[1])
arg2=int(sys.argv[2])
arg3=float(sys.argv[3])
print((arg1+arg2),(arg1*arg3),(arg2%arg1),(arg3//arg1))
one=(arg1+1)
two=(arg2+1)
three=(arg3+1)
print(one>>3,two/2,one | two)
print(one+(len(sys.argv[1:4])))
