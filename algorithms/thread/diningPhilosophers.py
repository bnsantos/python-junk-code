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
        self.trials = 0
        self.dinners = 0

    def run(self):
        while self.running:
            time.sleep(random.uniform(1, 5))
            print 'Philosopher %s is hungry.' % self._id
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork1, self.fork2
        while self.running:
            self.trials += 1
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print 'Philosopher %s swapping forks. ' % self._id
            fork1, fork2 = fork2, fork1
        else:
            print '**Philosopher %s done eating. ' % self._id
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print 'Philosopher %s starts eating ' % self._id
        self.dinners += 1
        time.sleep(random.uniform(1, 5))
        print 'Philosopher %s finishes eating and leaves to think. ' % self._id

    def how_much(self):
        print 'Philosopher %s tried to eat %d but only ate %d. ' % (self._id, self.trials, self.dinners)


def dining_philosophers():
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel', 'Adam Smith', 'Plato', 'Confucius',
                         'Friedrich Nietzsche', 'Other')
    forks = [threading.Lock() for n in range(len(philosopher_names))]
    philosophers = [Philosopher(philosopher_names[i], forks[i % len(philosopher_names)],
                                forks[(i+1) % len(philosopher_names)]) for i in range(len(philosopher_names))]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(60)
    Philosopher.running = False
    print ("-----Now we're finishing.")
    time.sleep(5)
    for p in philosophers:
        p.how_much()

if __name__ == "__main__":
    dining_philosophers()