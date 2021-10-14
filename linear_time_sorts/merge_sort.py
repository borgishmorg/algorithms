def _merge_sort(array: list, start: int, stop: int, buffer: list):
    if stop - start < 2:
        return

    m = (start + stop) // 2
    _merge_sort(array, start, m, buffer)
    _merge_sort(array, m, stop, buffer)

    i, j = start, m

    for k in range(start, stop):
        if j == stop or i < m and array[i] < array[j]:
            buffer[k] = array[i]
            i += 1
        else:
            buffer[k] = array[j]
            j += 1

    for k in range(start, stop):
        array[k] = buffer[k]


def merge_sort(array: list):
    "merge_sort sort array inplace and return it"
    _merge_sort(array=array, start=0, stop=len(array), buffer=[None for _ in array])
    return array
