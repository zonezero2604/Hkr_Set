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

#The first line of each part contains (the space separated entries(các mục được phân tách = space) of
# the operation name and the length of the other set.

#Bài làm
input() # dòng số các elements trong chuổi => k qtrong
a = set(map(int,input().split(' ')))
n = int(input())
for i in range(n):
