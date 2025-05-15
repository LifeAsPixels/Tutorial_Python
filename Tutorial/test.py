def main():
    print(Prime_Numbers(1000))

def Prime_Numbers(count):
    '''Return a list of some count of prime numbers'''

    primes = [1, 2, 3]
    number = primes[-1]
    while len(primes) < count:
        factors = False
        number += 2
        for num in range(3, number // 2):
            if number % num == 0:
                factors = True
                break
        if not factors:
            primes.append(number)
    while len(primes) > count:
        primes.pop()
    return primes

if __name__ == "__main__":
    main()