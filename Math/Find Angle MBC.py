Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền sẽ có chiều dài bằng nửa cạnh huyền.
=>BM=MB => phi bằng tan(AB/BC)
import math
AB = int(input())
BC = int(input())
print(round(math.degrees(math.atan(AB/BC))),chr(176),sep='')
#176 là ascii của độ