def buble_sort(array: list):
    "buble_sort sorts array inplace"
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
