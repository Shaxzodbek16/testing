import multiprocessing
import time

def heavy_computation(n):
    result = 0
    for i in range(n):
        result += i ** 2
    print(f"Hisob-kitob tugadi: {n}")
    return result

if __name__ == "__main__":
    start_time = time.time()

    numbers = [10_000_000,100_000_00_0, 15_000_000_00, 18_000_000_0] * 20
    processes = []
    results = []

    with multiprocessing.Pool(processes=80) as pool:
        results.append(pool.map(heavy_computation, numbers))

    print(f"Barcha hisob-kitoblar bajarildi: {time.time() - start_time:.2f} soniya")
    print(results)
