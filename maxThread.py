#!/usr/bin/env python  
#coding=gbk  
  
import threading  
import time, random,  sys  
  
class Counter:  
    def __init__(self):  
        self.lock = threading.Lock()  
        self.value = 0  
  
    def increment(self):  
        self.lock.acquire()   
        self.value = value = self.value + 1  
        self.lock.release()  
        return value  
  
counter = Counter()  
cond = threading.Condition()  
  
class Worker(threading.Thread):  
  
    def run(self):  
        print self.getName(),  "-- created."  
        cond.acquire()  
        #for i in range(10):  
            # pretend we're doing something that takes 10?00 ms  
            #value = counter.increment()   
            # time.sleep(random.randint(10, 100) / 1000.0)  
        cond.wait()  
        #print self.getName(), "-- task", "finished"   
        cond.release()  
          
  
  
if __name__ == '__main__':  
      
        try:  
            for i in range(3500):  
                Worker().start() # start a worker  
        except BaseException,  e:  
            print "Exception: ", type(e),  e  
            time.sleep(5)  
            print "maxium i=",  i  
        finally:  
            cond.acquire()  
            cond.notifyAll()  
            cond.release()  
            time.sleep(3)  
            print threading.currentThread().getName(),  " quit"  