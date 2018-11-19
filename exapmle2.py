import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # Thread-x started
        print("{} finished!".format(self.getName()))             # Thread-x finished


def Main():
    for x in range(100):
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # Instantiate a thread and pass a unique ID to it
        mythread.start()


if __name__ == '__main__':
    Main()

