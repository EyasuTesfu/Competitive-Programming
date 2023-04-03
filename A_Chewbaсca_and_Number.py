# num = input()
# res = []
# for n in num:
#     if res:
#         if 9 - int(n) < int(n):
#             res.append(str(9-int(n)))
#         else:
#             res.append(str(int(n)))
#     else:
#         if 9 - int(n) < int(n) and 9 - int(n) != 0:
#             res.append(str(9-int(n)))
#         else:
#             res.append(str(int(n)))
# if int(("".join(res))) == 0:
#     print(num[-1])
# else:
#     print(int("".join(res)))
num = input()
res = []
for n in num:
    if res:
        if 9 - int(n) < int(n):
            res.append(str(9-int(n)))
        else:
            res.append(str(int(n)))
    else:
        if 9 - int(n) < int(n) and 9 - int(n) != 0:
            res.append(str(9-int(n)))
        else:
            res.append(str(int(n)))
print(int("".join(res)))