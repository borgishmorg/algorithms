def _hoar_sort_stack(array: list, start: int, stop: int):  # stop included
    tasks = [(start, stop)]

    while tasks:
        start, stop = tasks.pop()

        if start >= stop:
            continue

        l = start - 1
        m = start - 1
        r = stop + 1
        k = array[(start + stop) // 2]

        while m + 1 < r:
            if array[m + 1] < k:
                array[m + 1], array[l + 1] = array[l + 1], array[m + 1]
                l += 1
                m += 1
            elif array[m + 1] == k:
                m += 1
            else:
                array[m + 1], array[r - 1] = array[r - 1], array[m + 1]
                r -= 1

        tasks.append((start, l))
        tasks.append((r, stop))


def hoar_sort_stack(array: list):
    "hoar_sort_stack sort array inplace and return it"
    _hoar_sort_stack(array=array, start=0, stop=len(array) - 1)
    return array
