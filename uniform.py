import time

def measure_runtime(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.12f} seconds")
    return result

def arent_equal(a, b):
    count = 0
    for n in range(len(str(a)), len(str(b)) + 1):
        for x in range(1, 10):
            if a <= int(str(x) * n) <= b:
                count += 1
    return print(count)

while True:
    a = int(input("Enter a number (A): "))
    b = int(input("Enter a number (B): "))
    if 0 < a <= b <= 10**12:
        if a == b:
            print(1)
        else:
            measure_runtime(arent_equal, a, b)