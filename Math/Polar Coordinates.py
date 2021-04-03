import cmath
c = complex(input().strip())
# print(cmath.polar(c))
# input  1+2j
# (2.23606797749979, 1.1071487177940904)
res = cmath.polar(c)
print(res[0])
print(res[1])