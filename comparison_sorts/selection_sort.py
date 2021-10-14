def selection_sort(array: list):
    "selection_sort sorts array inplace"
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
