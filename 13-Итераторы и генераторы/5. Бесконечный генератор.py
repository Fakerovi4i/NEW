def endless_gen():
    cur_val = 0
    while True:
        yield cur_val
        cur_val += 1

endless = endless_gen()

for i in range(10):
    print(next(endless), end=" ")

print()

for i in range(10):
    print(next(endless), end=" ")