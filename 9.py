import random
import time
from itertools import islice

K = 6
SIZES = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
RUNS = 3
LOW = -10_000
HIGH = 10_000


def generate_array(n):
    values = list(range(LOW, HIGH + 1))
    return random.choices(values, k=n)


def method_sort(arr):
    data = arr[:]
    data.sort(reverse=True)
    return data[K - 1]


def method_top_array(arr):
    top = sorted(arr[:K], reverse=True)
    for x in islice(arr, K, None):
        if x > top[-1]:
            top[-1] = x
            top.sort(reverse=True)
    return top[-1]


def method_max_removal(arr):
    removed = []
    for _ in range(K - 1):
        m = max(arr)
        i = arr.index(m)
        removed.append((i, m))
        arr[i] = LOW - 1
    result = max(arr)
    for i, m in removed:
        arr[i] = m
    return result


def measure(func, arr):
    start = time.perf_counter()
    result = func(arr)
    end = time.perf_counter()
    return (end - start) * 1000, result


def main():
    methods = [method_sort, method_top_array, method_max_removal]
    table = []

    for n in SIZES:
        row = [n]
        times = [[] for _ in methods]
        arr = None
        for _ in range(RUNS):
            arr = None
            arr = generate_array(n)
            results = []
            for idx, func in enumerate(methods):
                t, r = measure(func, arr)
                times[idx].append(t)
                results.append(r)
            if len(set(results)) != 1:
                raise ValueError("Результати методів не збігаються")
        for t in times:
            avg = sum(t) / len(t)
            row.append((avg, t))
        table.append(row)
        print(f"Розмір {n} опрацьовано")

    print()
    header = f"{'Розмір':>12} | {'Спосіб 1 (Сортування)':^40} | {'Спосіб 2 (Масив)':^40} | {'Спосіб 3 (Максимальні елементи)':^40}"
    print(header)
    print("-" * len(header))
    for row in table:
        cells = []
        for avg, t in row[1:]:
            runs = " ".join(f"{x:.0f}" for x in t)
            cells.append(f"{avg:.0f}({runs})".center(40))
        print(f"{row[0]:>12} | " + " | ".join(cells))


if __name__ == "__main__":
    main()