def insertion_sort(array: list):
    "insertion_sort sorts array inplace"
    for j in range(1, len(array)):
        value = array[j]
        i = j - 1
        while i >= 0 and array[i] > value:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = value
