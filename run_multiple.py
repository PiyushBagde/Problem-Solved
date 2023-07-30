import time
import multiprocessing


def hold_for_while(seconds):
    print(f"sleeping {seconds} seconds")
    time.sleep(seconds)
    print('done sleeping')

p1 = multiprocessing.Process(target=hold_for_while, args=[1])
p2 = multiprocessing.Process(target=hold_for_while, args=[1])

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p1.join()

    
finish = time.perf_counter()
print('finished running after : ',finish)
