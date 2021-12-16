def prefix(s: str) -> list:
    if not s:
        return []
    L = [0] * len(s)
    for i in range(len(s) - 1):
        l = L[i]
        while l > 0 and s[i + 1] != s[l]:
            l = L[l - 1]
        if s[i + 1] == s[l]:
            L[i + 1] = l + 1
        else:
            L[i + 1] = 0
    return L


def knuth_morris_pratt(a: str, x: str):
    L = prefix(x)
    l = 0
    for i in range(-1, len(a) - 1):
        while l > 0 and x[l] != a[i + 1]:
            l = L[l]
        if x[l] == a[i + 1]:
            l += 1
        else:
            l = 0
        if l == len(x):
            return i + 2 - len(x)
    return -1
