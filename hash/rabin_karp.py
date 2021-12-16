MOD = 1_000_000_007
SIGMA = 256


def mod_pow(x: int, n: int) -> int:
    if n < 1:
        return 1
    if n == 1:
        return x % MOD

    x_pow_n_div_2 = mod_pow(x, n // 2)

    res = x_pow_n_div_2 * x_pow_n_div_2 % MOD
    if n % 2:
        res = res * x % MOD
    return res


def f(s: str) -> int:
    r = 0
    for c in s:
        r = (r * SIGMA + ord(c)) % MOD
    return r


def rabin_karp(a: str, x: str):
    fx = f(x)
    fa = f(a[: len(x)])

    sigma_pow = mod_pow(SIGMA, len(x) - 1)

    for i in range(len(a) - len(x) + 1):
        if fa == fx:
            flag = True
            for j in range(len(x)):
                if a[i + j] != x[j]:
                    flag = False
                    break
            if flag:
                return i
        if len(a) > len(x) + i:
            fa = ((fa - ord(a[i]) * sigma_pow) * SIGMA + ord(a[i + len(x)])) % MOD
    return -1
