#Tổ Hợp
from itertools import combinations
sk = input().split()
s = sk[0]
k = int(sk[1])
for i in range(1,k+1):
    output = list(combinations(sorted(s),i))
    for m in output:
        for n in m:
            print(n,end='')
        print()