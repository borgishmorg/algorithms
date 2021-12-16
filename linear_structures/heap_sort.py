from .binary_heap import BinaryHeap


def heap_sort(array: list):
    "heap_sort returns sorted array"
    heap = BinaryHeap()
    for val in array:
        heap.add(val)
    return [heap.get() for _ in array]
