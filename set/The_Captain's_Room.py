# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite(vô hạn) amount of rooms.
#
# One fine day, a finite(hữu hạn) number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where  ≠ .
#
# The Captain was given a separate room, and the rest(người còn lại) were given one room per group.
#
# Mr. Anant has an unordered(ko có thứ tự) list of randomly arranged room entries(mục). The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except(ngoại trừ) for the Captain's room(chỉ xuất hiện 1 lần).
#
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.
#
# Input Format
#
# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


k=int(input())
rooms = list(map(int, input().split()))
a=set()
b=set()
for room in rooms:
	if room not in a:
		# thêm room vào list a trùng thì ko thêm  nữa
		a.add(room)
		b.add(room)
	else:
		# có trong a thì xóa phần tử đó trong b (discard ko gán ra 1 biến riêng được vì nó k trả về j)
		b.discard(room)
output = list(b)
print(output[0])