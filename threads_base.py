import threading
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(5)
    print(f"\nTask {name} finished")

thread1 = threading.Thread(target=task, args=("Thread 1",))
thread2 = threading.Thread(target=task, args=("Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All process are finished!")