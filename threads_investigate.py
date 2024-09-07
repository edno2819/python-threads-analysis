import threading
import time

start_time = None

def increment_counter():
    global start_time
    counter = 0
    for _ in range(10**6):
        counter += 1
    finished_time_thread = time.time() - start_time
    print(f"Time {finished_time_thread:.2f} seconds - Thread finished! Counter value - {counter}")


def run_threads():
    global start_time

    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    run_threads()
