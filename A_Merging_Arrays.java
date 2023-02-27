n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
merged = []
p1, p2 = 0
while(p1 < len(num1) and p2 < len(num2)):
    if num1[p1] > num2[p2]:
        merged.append(num2[p2])
        p2 += 1
    else:
        merged.append(num1[p1])
        p1 += 1
while p1 < len(num1):
    merged.append(num1[p1])
    p1 += 1
elif p2 < len(num2):
    merged.append(num2[p2])
    p2 += 1
return " ".join(merged)