#!/usr/bin/python3
def main():
    f = open("tests/test00", "r")
    for x in f:
        num = int(x)
        prime = get_smallest_prime(num)
        other = int(num/prime)
        print(f"{num}={other}*{prime}")


def get_smallest_prime(num):
    from math import sqrt
    if num % 2 == 0:
        return 2
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            return i
if __name__ == "__main__":
    main()
