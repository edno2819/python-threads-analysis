import multiprocessing
import time

start_time = None

def increment_counter():
    global start_time
    counter = 0
    for _ in range(10**6):
        counter += 1
    finished_time_process = time.time() - start_time
    print(f"Time {finished_time_process:.2f} seconds - Process finished! Counter value - {counter}")


def run_processes():
    global start_time

    process1 = multiprocessing.Process(target=increment_counter)
    process2 = multiprocessing.Process(target=increment_counter)

    start_time = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    run_processes()
