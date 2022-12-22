# problem link:https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
room_dict = {}
k = int(input())
room_list = list(input().split())
for i in room_list:
    if i not in room_dict:
        room_dict[i] = 1
    else:
        room_dict[i] += 1
for i in room_dict.keys():
    if room_dict[i] != k:
        print(i)
        break
# -------------------prefix sum-----------------
K = int(input())
Rooms = list(map(int, input().split()))
RoomNum = set(Rooms)

IdealRoomTotal = sum(RoomNum)*K
RealRoomTotal = sum(Rooms)

CaptainRoom = (IdealRoomTotal-RealRoomTotal)//(K-1)
print(CaptainRoom)
