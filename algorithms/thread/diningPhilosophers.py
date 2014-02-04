__author__ = 'bruno'
import threading
import random
import time


class Philosopher(threading.Thread):
    running = True

    def __init__(self, _id, fork1, fork2):
        threading.Thread.__init__(self)
        self._id = _id
        self.fork1 = fork1
        self.fork2 = fork2

    def run(self):
        while self.running:
            time.sleep(random.uniform(3, 13))
            print 'Philosopher %s is hungry.' % self._id
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork1, self.fork2
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print 'Philosopher %s swapping forks. ' % self._id
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print 'Philosopher %s starts eating ' % self._id
        time.sleep(random.uniform(1, 10))
        print 'Philosopher %s finishes eating and leaves to think. ' % self._id


def dining_philosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel')
    philosophers = [Philosopher(philosopher_names[i], forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(20)
    Philosopher.running = False
    print ("Now we're finishing.")

if __name__ == "__main__":
    dining_philosophers()