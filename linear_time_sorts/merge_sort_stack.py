def merge_sort_stack(array: list):
    "merge_sort sort array inplace and return it"

    buffer = [None for _ in array]
    to_sort_stack = list()
    to_merge_stack = list()

    to_sort_stack.append((0, len(array)))

    while len(to_sort_stack) > 0 or len(to_merge_stack) > 1:
        if len(to_merge_stack) > 1:
            first_start, first_stop = to_merge_stack.pop()
            second_start, second_stop = to_merge_stack.pop()

            start, stop = first_start, second_stop
            i, j = first_start, second_start

            for k in range(start, stop):
                if j == second_stop or i < first_stop and array[i] < array[j]:
                    buffer[k] = array[i]
                    i += 1
                else:
                    buffer[k] = array[j]
                    j += 1

            for k in range(start, stop):
                array[k] = buffer[k]

            to_merge_stack.append((start, stop))
        elif len(to_sort_stack) > 0:
            to_sort_start, to_sort_stop = to_sort_stack.pop()
            if to_sort_stop - to_sort_start < 2:
                to_merge_stack.append((to_sort_start, to_sort_stop))
            else:
                m = (to_sort_start + to_sort_stop) // 2
                to_sort_stack.append((to_sort_start, m))
                to_sort_stack.append((m, to_sort_stop))

    return array
