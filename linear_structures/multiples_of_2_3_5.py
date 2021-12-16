def multiples_of_2_3_5(n: int) -> list[int]:
    res = []

    multiples_of_2 = [2]
    multiples_of_3 = [3]
    multiples_of_5 = [5]

    for _ in range(n):
        if multiples_of_2[0] <= min(multiples_of_3[0], multiples_of_5[0]):
            value = multiples_of_2.pop(0)
            res.append(value)

            multiples_of_2.append(value * 2)
            multiples_of_3.append(value * 3)
            multiples_of_5.append(value * 5)
        elif multiples_of_3[0] <= min(multiples_of_2[0], multiples_of_5[0]):
            value = multiples_of_3.pop(0)
            res.append(value)

            multiples_of_3.append(value * 3)
            multiples_of_5.append(value * 5)
        else:
            value = multiples_of_5.pop(0)
            res.append(value)

            multiples_of_5.append(value * 5)

    return res


if __name__ == "__main__":
    print(*multiples_of_2_3_5(100))
