import multiprocessing as mp
import numpy as np
import tqdm


def sigma(process, lower, upper, output):
    summation = 0

    if process == 0:
        iterator = tqdm.trange(lower, upper, 2, unit="div")
    else:
        iterator = range(lower, upper, 2)

    for x in iterator:
        summation += 4 / (2 * x - 1)
        summation -= 4 / (2 * x + 1)

    output.put(summation)


def main():
    output = mp.Queue()

    iterations = 10 ** 10
    cpus = mp.cpu_count()
    remainder = iterations % cpus
    block = int((iterations - remainder) / cpus)

    processes = [mp.Process(target=sigma, args=(process, process * block + 1, (process + 1) * block + 1, output))
                 for process in range(cpus)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes if p is not None]

    print(str.format("{0:.100f}", np.sum(results)))
    print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")


if __name__ == "__main__":
    main()
    # 10,403s with 10^9 iterations
