def fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    s = [1 for _ in range(n + 1)]

    for i in range(2, n + 1):
        s[i] = s[i - 1] + s[i - 2]

    return s[n]


if __name__ == "__main__":
    for i in range(25):
        print(f"fib({i:2}) = {fibonacci(i):5}")
