from multiprocessing import Pool
from time import sleep

def target_fun(instance):
    print(instance)
    #print(threading.active_count())
    sleep(3)
    print(instance)
    #print(threading.active_count())

instances = ['i1', 'i2','i3','i4','i5','i6','i7','i8','i9','i10']

pool = Pool(processes=5)              # start 4 worker processes
pool.map(target_fun, instances)

print("END LINE")
