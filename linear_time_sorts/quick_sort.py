def _quick_sort(array: list, start: int, stop: int):  # stop included
    if start >= stop:
        return

    m = (start + stop) // 2

    if min(array[start], array[stop]) <= array[m] <= max(array[start], array[stop]):
        p = array[m]
    elif min(array[m], array[stop]) <= array[start] <= max(array[m], array[stop]):
        p = array[start]
    else:
        p = array[stop]

    l = start - 1
    r = stop + 1

    while True:
        while True:
            l += 1
            if array[l] >= p:
                break
        while True:
            r -= 1
            if array[r] <= p:
                break
        if l >= r:
            break
        array[l], array[r] = array[r], array[l]

    _quick_sort(array, start, r)
    _quick_sort(array, r + 1, stop)


def quick_sort(array: list):
    "quick_sort sort array inplace and return it"
    _quick_sort(array=array, start=0, stop=len(array) - 1)
    return array
