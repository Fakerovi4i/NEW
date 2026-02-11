
import random
class My_iter_class:
    def __init__(self, q_elem):
        self.q_elem = q_elem

    def __iter__(self):
        self.current_val = random.random()
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.q_elem:
            raise StopIteration
        if self.counter > 1:
            self.current_val += random.random()
        return self.current_val

my = My_iter_class(5)

for i in my:
    print(i)





















