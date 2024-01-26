#!/usr/bin/python3
def main():
    import sys
    file = sys.argv[1]
    f = open(file, "r")
    for x in f:
        num = int(x)
        prime = get_smallest_prime(num)
        other = int(num/prime)
        print(f"{num}={other}*{prime}")
    f.close()


def get_smallest_prime(num):
    from math import sqrt
    if num % 2 == 0:
        return 2
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            return i


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print(end - start)

