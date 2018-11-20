from threading import Thread
import threading
from time import sleep

def target_fun(instance):
    print(instance)
    #print(threading.active_count())
    sleep(3)
    print(instance)
    #print(threading.active_count())

instances = ['i1', 'i2','i3','i4','i5','i6','i7','i8','i9','i10']
threads = []
for instance in instances:
    t1 = Thread(target=target_fun, args=(instance,))
    #t1.run()     # Which takes considerable time
    t1.start()   # With help of threading , executio will be faster
    threads.append(t1)
for thread in threads:
    thread.join()
print("End of the Function")

