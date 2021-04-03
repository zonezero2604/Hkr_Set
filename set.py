############   Set Mutations   ##############

#We can use the following operations(phép toán) to create mutations(đột biến-thay đổi) to a set:
#.update() or |=
'''H = set("Hacker")
R = set("Rank")
C=H|R
print(C)
print(H)
H.update(R)
print(H)'''
'''(testpython) F:\forpython\testpython>python set.py
{'r', 'R', 'n', 'c', 'e', 'H', 'a', 'k'}
{'r', 'c', 'e', 'H', 'a', 'k'}
{'r', 'R', 'n', 'c', 'e', 'H', 'a', 'k'}'''


#.intersection_update() or &=
'''>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])'''

#.difference_update() or -=
#Update the set by removing elements found in an iterable/another set.
'''>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])'''

#.symmetric_difference_update() or ^=
#Update the set by only keeping the elements found in either set, but not in both.
'''>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])'''

#The first line contains the number of elements in set A
#The second line contains the space separated list of elements in set A
#The third line contains integer N , the number of other sets.
#The next 2*N lines are divided into N parts containing two lines each.
	#The first line of each part contains (the space separated entries(các mục được phân tách = space) of
	# the operation name and the length of the other set.
	#The second line of each part contains space separated list of elements in the other set.

# sample input
 # 16
 # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 # 4
 # intersection_update 10
 # 2 3 5 6 8 9 1 4 7 11
 # update 2
 # 55 66
 # symmetric_difference_update 5
 # 22 7 35 62 58
 # difference_update 7
 # 11 22 35 55 58 62 66
 #Sample Output
 #38
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Bài làm
def Operations():
	# define biến toàn cục
	global output
	
	#nhập vào text lệnh và số các phân tử của moudel set
	# lấy các giá trị nhập vào cách nhau nhiều dấu cách cũng thành 1 dấu cách và dạng LIST
	ol = input().split()
	# lấy text lệnh
	operation = ol[0]
	# dòng 2 nhập các phần tử của module set
	updaterSet = set(map(int,input().split(' '))) 
	if operation == 'intersection_update':
		a.intersection_update(updaterSet)
	elif operation == 'update':
		a.update(updaterSet)
	elif operation == 'symmetric_difference_update':
		a.symmetric_difference_update(updaterSet)
	elif operation == 'difference_update':
		a.difference_update(updaterSet)
	output=sum(a)
	return 


# dòng số các elements trong chuỗi => k qtrong
input() 

# các phần tử của main set
# lấy set từ các giá trị nhận vào cách nhau dấu cách và chuyển về int hết
# split(' ') nếu giữ 2 từ có 3 dấu cách thì sẽ có 2 phần tử ''
# a a  a   a    a
# ['a', 'a', '', 'a', '', '', 'a', '', '', '', 'a']
a = set(map(int,input().split()))

#số lên được thực hiện bên trong
n = int(input())

# N dong lệnh
for i in range(n):
	Operations()
print(output)

