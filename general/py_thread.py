""" A python threading """

import os
import threading
import time

class PyThread(threading.Thread):
    def __init__(self, delay_seconds=0.500):
        print("Thread init is called...")

        self._delay = delay_seconds
        self._stop_event = threading.Event()
        threading.Thread.__init__(self)

    def run(self):
        print("Thread run is called...")

        while not self._stop_event.isSet():
            self._stop_event.wait(self._delay)
           
        print("Thread run is finished...")

    def stop(self):
        self._stop_event.set()

# Python thread
print("Create a thread")
thread = PyThread()

print("Start thread")
thread.start()
if thread.is_alive():
    time.sleep(0.5 * 60)

print("Ask to stop thread")
thread.stop()

print("Wait for thread shutdown")
thread.join()

print("Done")
