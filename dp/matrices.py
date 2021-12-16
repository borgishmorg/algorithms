v = [10, 30, 5, 60]
dp = [[-1 for _ in range(len(v))] for _ in range(len(v))]


def matrices(l: int, r: int):
    if dp[l][r] == -1:
        if l == r - 1:
            dp[l][r] = 0
        else:
            dp[l][r] = 10 ** 9
            for i in range(l + 1, r):
                dp[l][r] = min(
                    dp[l][r],
                    v[l] * v[i] * v[r] + matrices(l, i) + matrices(i, r),
                )
    return dp[l][r]


print(matrices(0, len(v) - 1))
