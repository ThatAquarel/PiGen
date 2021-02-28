def sigma(iterations):
    summation = 0
    for x in range(1, iterations + 1):
        # sum += 8 / (16 * x * x - 16 * x + 3)
        # 264,568s with 10^9 iterations

        # summation = summation + 4 / (2 * x - 1) * (-1) ** (x + 1)
        # 337,444s with 10^9 iterations

        div = x % 2
        if div == 0:
            div = -1

        summation += 4 / (2 * x - 1) * div
        # 127,910s with 10^9 iterations
    return summation


if __name__ == '__main__':
    print(sigma(10 ** 9))
