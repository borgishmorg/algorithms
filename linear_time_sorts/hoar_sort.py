def _hoar_sort(array: list, start: int, stop: int):  # stop included
    if start >= stop:
        return

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

    _hoar_sort(array, start, l)
    _hoar_sort(array, r, stop)


def hoar_sort(array: list):
    "hoar_sort sort array inplace and return it"
    _hoar_sort(array=array, start=0, stop=len(array) - 1)
    return array
