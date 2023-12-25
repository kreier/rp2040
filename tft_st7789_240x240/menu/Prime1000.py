import math, time
last = 1000
found = 4          # we start from 11, know 2, 3, 5, 7
print(f"Primes to {last}")
print('2, 3, 5, 7',end='')
start = time.monotonic()
for number in range(11, last, 2):
    prime = True
    for divider in range(3, int(math.sqrt(number))+1, 2):
        if number % divider == 0:
            prime = False
            break
    if prime:
        print(",", number, end='')
        found += 1
        prime = 1
end = time.monotonic()
print(f"\nIt took: {(end - start)} s.")
print(f"Found {found} numbers.")

time.sleep(5)
