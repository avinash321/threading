from threading import Thread
from time import sleep
class Test1(Thread):
    def run(self):
        for i in range(3):
            print("METHOD 1")
            sleep(1)

class Test2(Thread):
    def run(self):
        for i in range(3):
            print("METHOD 2")
            sleep(1)

t1 = Test1()
t2 = Test2()

t1.start()
t2.start()

t1.join()
t2.join()

print("Task Completed!")
