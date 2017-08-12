number = 0

def main():

    list = [0, 1, 2, 3, 4, 8, 7, 9, 3, 2, 10, 11, 40, 102, 2, 4, 6, 99]

    largest(list)


def largest(list):

    number = list[0]

    while len(list) > 1:

        if number < list[1]:

            list.remove(number)
            number = list[0]

        else:

            del list[1]

        if len(list) == 1:
            print("The largest number in the list is", number)

        #print(number)

        largest(list)

main()