def main():

    m = 10
    n = 20

    value = ackermann(m, n)

    print(value)


def ackermann(m, n):

    if m == 0:
        return 1
    if n == 0:
        return ackermann(m - 1, n)
    else:
        return ackermann(m - 1, ackermann(m, n-1))

main()