from random import random, seed

seed(0)

TEST_ARRAYS = [
    [[], []],
    [[2, 1], [1, 2]],
    [[1, 2, 3], [1, 2, 3]],
    [[3, 2, 1], [1, 2, 3]],
    [[i for i in range(1000, -1, -1)], [i for i in range(0, 1001)]],
]

for size in (100, 200, 500, 1000, 2000, 10000, 100000, 1000000):
    RANDOM_ARRAY = [200 * random() - 100 for _ in range(size)]
    SORTED_RANDOM_ARRAY = [*sorted(RANDOM_ARRAY)]
    TEST_ARRAYS.append([RANDOM_ARRAY, SORTED_RANDOM_ARRAY])
