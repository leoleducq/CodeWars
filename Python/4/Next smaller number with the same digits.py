def next_smaller(n):
    n = list(str(n))
    liste = []
    for i in range(len(n)-2, -1, -1):
        if n[i] > n[i+1]:
            for j in range(len(n)-1, i, -1):
                if n[j] < n[i]:
                    n[i], n[j] = n[j], n[i]
                    liste = int(''.join(n[:i+1] + sorted(n[i+1:], reverse=True)))
                    if len(str(liste)) != len(n):
                        return -1
                    return liste
    return -1