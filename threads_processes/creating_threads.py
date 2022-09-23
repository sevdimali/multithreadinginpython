import time
from threading import Thread


def do_work():
    print("Starting work")
    # time.sleep(1)
    i=0
    for _ in range(900000000):
        i = i+1
    print("Finished work")


for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()

