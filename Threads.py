import queue
from threading import Thread
from queue import Queue
from time import sleep
import random
import colorama
from colorama import Fore

class Producer:
    def __init__(self,q):
        self.q = q

    def produce(self):
        for i in range (1,101):
            x=random.randint(1,500)
            print(f"{Fore.GREEN}Item Produced : ",x)
            self.q.put(x)
            sleep(1)
            
class Consumer:
    def __init__(self,prod):
        self.prod=prod

    def consume(self):
        for i in range (1,101):
            print(f"{Fore.RED}Item Consumed : ",self.prod.q.get())
            list1 = [1, 2, 3, 4, 5]
            sleep(random.choice(list1))

q=queue.Queue()
p=Producer(q)
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()

t1.join()
t2.join()
