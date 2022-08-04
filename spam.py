import time
import sys
import tty
from threading import Thread

def thegood():
    tty.setraw(sys.stdin.fileno())
    while True:
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(0.08)

for i in range(1000):
    t = Thread(target=thegood)
    t.start()