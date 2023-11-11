import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result
def example_function():
    time.sleep(2)
if __name__ == "__main__":
    elapsed_time, result = measure_time(example_function)
    print(f"Час виконання example_function: {elapsed_time} секунд")
    print(f"Результат example_function: {result}")