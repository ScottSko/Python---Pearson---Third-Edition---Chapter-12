def main():

    int = 743
    total = 0

    int_sum(int, total)

def int_sum(int, total):

    total += int

    int -= 1

    if int > 0:
        int_sum(int, total)
    else:
        print("The sum is", total)

main()