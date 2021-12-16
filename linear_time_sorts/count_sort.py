def count_sort(array: list):
    "count_sort returns sorted array"
    if not array:
        return []

    cnt = [0] * (max(array) + 1)

    for a in array:
        cnt[a] += 1

    return [num for num, count in enumerate(cnt) for _ in range(count)]
