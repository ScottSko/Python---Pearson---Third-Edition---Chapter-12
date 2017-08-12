def main():

    n = 10
    number = 0

    lines(n, number)

def lines(n, number):

    if n > 0:

        n -= 1
        number += 1

        # Without recursion, you could just uncomment the loop and it would work fine.
        # Recursion takes the place of the second loop.

        for y in range(number):
            #for z in range(y + 1):
            print("*", end='')
        print()

        lines(n, number)

main()