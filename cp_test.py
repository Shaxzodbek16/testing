import multiprocessing
import time

def heavy_computation(n):
    sum = 0
    for i in range(n):
        sum += i ** 2
    return sum

if __name__ == "__main__":
    start_time = time.time()

    N = 10_000_000  # Katta son
    cpu_count = multiprocessing.cpu_count()
    print(f"Kompyuterda {cpu_count} ta yadro bor!")

    with multiprocessing.Pool(processes=cpu_count) as pool:
        results = pool.map(heavy_computation, [N] * cpu_count)

    print(f"Barcha hisob-kitoblar {time.time() - start_time:.2f} soniyada tugadi")