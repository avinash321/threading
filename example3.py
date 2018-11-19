from threading import Thread
import threading
from time import sleep

def target_fun(i):
    print(i + "  target function")
    print(threading.active_count())
    sleep(3)
    print(i + "  task completed")
    print(threading.active_count())


l = ['abc','def','xyz','ramu','somu','ravi','ajay']
for i in l:
    t1 = Thread(target=target_fun,args=(i,))
    #t1.run()     # Which takes considerable amount of time
    t1.start()   # With help of threading , execution will be faster






