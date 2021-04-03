# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# output
# True
# False
# False
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def checker():
    # nhập số phần tử set 1
    x = int(input())
    # nhập set 1
    s1 = set(map(int, input().split()))
    # nhập số phần tử set 2
    y = int(input())
    # nhập set 2
    s2 = set(map(int, input().split()))
    # nếu tất cả các phần tử trong set 1 trùng với tất  cả phần tử trong set 2 => set 1 là subset của set 2
    l = []
    for i in s1:
        if i in s2:
            l.append(i)
    l = set(l)
    if l == s1:
        print('True')
    else:
        print('False')

# hàm main
n = int(input())
for i in range(n): # vd nhập n = 5 range(n) = (0,5)
    checker()