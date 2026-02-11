# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который
# принимает максимальное число N и выдаёт все простые числа от 1 до N.

class Primes:
    def __init__(self, max):
        self.__max = max
        self.counter = 2

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.counter <= self.__max:
            num = self.counter
            self.counter += 1
            if self.is_prime(num):
                return num
        raise StopIteration

# Основной код:
prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
