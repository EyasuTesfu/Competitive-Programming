def superDigit(n, k):
    if k*len(n) == 1:
        return n
    _sum = 0
    for i in range(len(n)):
        _sum += int(n[i])
    _sum *= k
    return superDigit(str(_sum), 1)
