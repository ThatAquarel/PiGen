def sigma(iterations):
    summation = 0
    for x in range(1, iterations + 1, 2):
        summation += 4 / (2 * x - 1)
        summation -= 4 / (2 * x + 1)
        # 73,103s with 10^9 iterations

        # summation += 8 / (4 * x * x - 1)
        # 107,736s with 10^9 iterations
    return summation


if __name__ == '__main__':
    print(sigma(10 ** 9))
