def main():
    n = 5

    traffic_sign(n)


def traffic_sign(n):
    while n > 0:
        print(n)
        print("No Parking")
        n = n > 1

        print(n)


main()