n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
p1, p2 = 0, 0
res = []
while (p1 < len(num1) and p2 < len(num2)):
    while p1 < len(num1) and num2[p2] > num1[p1]:
        p1 += 1
    res.append(p1)
    p2 += 1
if p1 == len(num1):
    for i in range(p2, len(num2)):
        res.append(p1)
print(str(res).strip("[]").replace(",", ""))
