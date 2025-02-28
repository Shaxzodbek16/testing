import threading
import multiprocessing
import time

def count(n):
    while n > 0:
        n -= 1

N = 50_000_000_000

def main()-> None:
    start = time.time()
    t1 = threading.Thread(target=count, args=(N,))
    t2 = threading.Thread(target=count, args=(N,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Multithreading vaqti: {time.time() - start:.2f} soniya")

    start = time.time()
    p1 = multiprocessing.Process(target=count, args=(N,))
    p2 = multiprocessing.Process(target=count, args=(N,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Multiprocessing vaqti: {time.time() - start:.2f} soniya")
if __name__ == '__main__':
    main()
