from random import random, seed, sample

seed(0)

TEST_ARRAYS = [
    [[], []],
    [[2, 1], [1, 2]],
    [[1, 2, 3], [1, 2, 3]],
    [[3, 2, 1], [1, 2, 3]],
    [[i for i in range(1000, -1, -1)], [i for i in range(0, 1001)]],
    [[*sample(range(1000, -1, -1), 1001)], [i for i in range(0, 1001)]],
    [[*sample(range(100000, -1, -1), 100001)], [i for i in range(0, 100001)]],
]

for size in (100, 200, 500, 1000, 2000, 10000, 100000, 1000000):
    RANDOM_ARRAY = [200 * random() - 100 for _ in range(size)]
    SORTED_RANDOM_ARRAY = [*sorted(RANDOM_ARRAY)]
    TEST_ARRAYS.append([RANDOM_ARRAY, SORTED_RANDOM_ARRAY])
