total = 1

def main():

    number = 4
    exponent = 4
    #total = 1

    exponential(number, exponent, total)


def exponential(number, exponent, total):

    total *= number

    exponent -= 1

    if exponent == 0:
        print(total)
    else:
        exponential(number, exponent, total)

main()