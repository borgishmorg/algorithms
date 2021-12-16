from collections import defaultdict


def prefix(s: str) -> list:
    if not s:
        return 0
    L = [0] * len(s)
    for i in range(len(s) - 1):
        l = L[i]
        while l > 0 and s[i + 1] != s[l + 1]:
            l = L[l]
        if s[i + 1] == s[l + 1]:
            L[i + 1] = l + 1
        else:
            L[i + 1] = 0
    return L


def rights(x: str) -> dict:
    right = defaultdict(lambda: -1)
    for i, c in enumerate(x):
        right[c] = i
    return right


def jumps(x: str) -> list:
    L_x = prefix(x)
    x_r = [*reversed(x)]
    L_x_r = prefix(x_r)

    jump = [0] * len(x)

    for i in range(len(x)):
        jump[i] = len(x) - L_x[len(x) - 1]  # +-1
    for lmbda in range(len(x)):
        i = len(x) - L_x_r[len(x) - 1] - 1  # +-1
        jump[i] = min(jump[i], lmbda - L_x_r[lmbda])
    return jump


def boyer_moore(a: str, x: str):
    right = rights(x)
    jump = jumps(x)

    s = -1

    while s <= len(a) - len(x):  # +- 1
        j = len(x) - 1
        while j >= 0 and x[j] == a[s + j]:
            j -= 1
        if j == -1:
            return s
        delta = max(
            0,
            1,
            j - right[a[s + j]] - 1,
            jump[j],
        )
        s += delta

    return -1
