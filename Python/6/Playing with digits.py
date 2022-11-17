def dig_pow(n, p):
    list = [int(i) for i in str(n)]
    res = sum([list[i] ** (p + i) for i in range(len(list))])
    return int(res / n) if res % n == 0 else -1