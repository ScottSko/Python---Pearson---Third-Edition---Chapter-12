n = 10
number = 0

def main():

    print_n(n, number)

def print_n(n, number):
    number += 1
    print(number)

    n -= 1
    if n > 0:
        print_n(n, number)

main()
