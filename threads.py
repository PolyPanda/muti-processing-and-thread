# threads demo

import time
import random
import threading
import queue
import tkinter as tk

random.seed()

# simulation of a long running or slow task
def slowFunction(sleepTime) :
    print(threading.currentThread().getName(), "is running slow task")
    print("slow task is running")
    time.sleep(sleepTime)       # sleep time is in seconds
    print(random.randint(1,10))

'''
# no threads
start = time.time()

for i in range(4) :          # need to run the slow task 4 times
    slowFunction(5)

print("Elapsed time: %.2f" % float((time.time()-start)))

for count in range(20) :     # and print 20 numbers
    print(count, end=" ")
print()                      # printing 20 numbers has to come after
                             # the slow task
                             
for count in range(10) :     # print 10 numbers as the last task
    print(count, end=" ")
print()
'''
'''
# with threads
start = time.time()

threads = []
for i in range(4) :          # need to run the slow task 4 times
    t = threading.Thread(target = slowFunction, args = (10, ))
    threads.append(t)
    t.start()                # get 4 threads to run 
    
for count in range(20) :     # and print 20 numbers
    print(count, end=" ")
print()                      # can print the 20 numbers while threads
                             # run

for t in threads :
    t.join()                 # wait for thread to finish

print("Elapsed time: %.2f" % float((time.time()-start)))

for count in range(10) :     # print 10 numbers as the last task
    print(count, end=" ")
print()
'''
'''
# naming threads
t1 = threading.Thread(target=slowFunction, args=(4,), name='thread 1')
t1.start()
t2 = threading.Thread(target=slowFunction, args=(4,), name='thread 2')
t2.start()
t1.join()
t2.join()
'''
'''
# daemon thread
d = threading.Thread(target=slowFunction, args=(2,))
d.setDaemon(True)
d.start()
time.sleep(4)    # if sleep time here is shorter than sleep time of daemon
                 # we won't see the random num printed
                 # but if sleep time is longer, then we see the random num
'''
'''
# join with timer
t = threading.Thread(target=slowFunction, args=(8,))
t.start()
t.join(2.0)           # set timer for main thread to continue
                      # regardless of whether the child thread is done
print(t.isAlive())    # check to see if child thread is done (return False)
                      # or the timer times out (True)              
'''
'''
# enumerate
t1 = threading.Thread(target=slowFunction, args=(3,))
t2 = threading.Thread(target=slowFunction, args=(3,))
d = threading.Thread(target=slowFunction, args=(3,))
d.setDaemon(True)
t1.start()
t2.start()
d.start()
for t in threading.enumerate() :
    print(t.getName())
    
t1.join()
t2.join()
'''
'''
# Event
def blockingWait(e):
    print(threading.currentThread().getName(), ": blockingWait start, waiting for event flag set")
    wait = e.wait()
    print(threading.currentThread().getName(), ": event flag set, do work")

def nonBlockingWait(e, t):
    print(threading.currentThread().getName(), "nonBlockWait start")
    while not e.isSet():
        wait = e.wait(t)    # wait for t seconds
        print(threading.currentThread().getName(), "flag status:", wait)
        if wait:
            print(threading.currentThread().getName(), ": event flag set, do work")
        else:
            print(threading.currentThread().getName(), ": do something while waiting")

e = threading.Event()       # create Event object
# create thread and start it
#t1 = threading.Thread(target=blockingWait, args=(e,))
t1 = threading.Thread(target=nonBlockingWait, args=(e,1.5))
t1.start()

print("main thread before setting event")
time.sleep(5)
e.set()   
print("main thread setting event")

t1.join()
print("main thread done")
'''
'''
# race condition
class Counter() :
    def __init__(self) :
        self.counter = 0
    def inc(self) :
        for x in range(200000):    # add 1 to total for a while
            self.counter += 1
    def printCount(self) :
        print(self.counter)
  
c = Counter()       # c is a shared resource
threads = []
for i in range(4) :     # create 4 threads to add to counter
    t = threading.Thread(target=c.inc)
    threads.append(t)

start = time.clock()
for t in threads :      # start 4 threads
    t.start()

for t in threads :      # wait for them to end
    t.join()
    
diff = time.clock() - start

c.printCount()
print(diff)
'''
'''
# fix race condition with Locks
class Counter() :
    def __init__(self) :
        self.counter = 0
        self.lock = threading.Lock()
    def inc(self) :
        #self.lock.acquire()
        with self.lock :
            for x in range(200000):    # add 1 to total for a while
                self.counter += 1
        #self.lock.release()
    def printCount(self) :
        print(self.counter)
  
c = Counter()       # c is a shared resource
threads = []
for i in range(4) :     # create 4 threads to add to counter
    t = threading.Thread(target=c.inc)
    threads.append(t)

start = time.clock()
for t in threads :      # start 4 threads
    t.start()
    
for t in threads :      # wait for them to end
    t.join()
diff = time.clock() - start

c.printCount()
print(diff)
'''
'''
# queue
def getData():
    for i in range(10) :
        if not q.empty() :
            item = q.get()
            print(i, "getting:", item)
            time.sleep(2)
        
def putData():
    for i in range(10) :
        num = random.randint(1,10)
        if not q.full() :
            q.put(num)
            print(i, "putting in queue")
            time.sleep(1)

q = queue.Queue()
p = threading.Thread(target=putData)
p.start()
c = threading.Thread(target=getData)
c.start()

# stop workers
p.join()
c.join()

print("main done")
'''
'''
#semaphore
def doWork(s):
    print(threading.currentThread().getName(), "waiting for resource")
    with s:
        print(threading.currentThread().getName(), "got resource")
        time.sleep(2)

s = threading.Semaphore(3)
threads = []
for i in range(8):
    t = threading.Thread(target=doWork, name="thread "+str(i), args=(s,))
    threads.append(t)
    t.start()

for i in threads :
    t.join()
print("main done")
'''
'''
# tkinter after()

class TestWin(tk.Tk):
    def __init__(self) : 
        super().__init__()

        self.V = tk.IntVar()    # count var
        self.V.set(100)
                           
        B = tk.Button(self, text="Count", command=self.countUp)  # button to count up
        B.grid(sticky='w')        

        L = tk.Label(self, textvariable=self.V, width=25)  # display var
        L.grid(row=0, column=1, sticky='ew') 
        
        #B = tk.Button(self, text="Cancel Reset", command=self.cancel)  # button to count up
        #B.grid(sticky='w')         
        
        self.after(1000, self.clear)
        
    def countUp(self) :
        self.V.set(self.V.get() + 1)
        
    def clear(self) :
        self.V.set(0)
        self.id = self.after(10000, self.clear)
        print("next reset by", self.id)

    """
    def cancel(self) :
        self.after_cancel(self.id)
        print("cancel", self.id)
    """
        
t = TestWin()
t.mainloop()
'''
