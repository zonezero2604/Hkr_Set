# The first line contains the space separated elements of set A .
# The second line contains integer n , the number of other sets.
# The next n lines contains the space separated elements of the other sets.

# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# input
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# output
# false


# Tập cha
def checker():
	# Nhập others set
	sub = set(map(int, input().split()))
	# nếu other set là tập con của set s1 thì l1=1 print true 
	if sub.issubset(s1):
		if len(sub) == len(s1):
			l.append(0)
		else:
			l.append(1)
	else:
		l.append(0)
		#trường hợp cả 2 set bằng nhau nhưng cùng độ dài thì cũng k phải  là tập cha
s1 = set(map(int, input().split()))
n=int(input())
l=[]
for i in range(n):
	checker()
if all(l) == 1 :
	print(True)
else:
	print(False)