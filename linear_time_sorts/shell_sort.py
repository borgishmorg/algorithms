def shell_sort(array: list):
    "shell_sort sort array inplace and return it"
    last_index = len(array) - 1
    step = len(array) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
        step //= 2
    return array
