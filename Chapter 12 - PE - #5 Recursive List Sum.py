index = 0
total = 0
list = [0, 1, 2, 3, 4, 100]

def main():

    sum(list, index, total)

def sum(list, index, total):

    total += list[index]

    index += 1

    if len(list) > index:

        sum(list, index, total)

    else:
        print("The sum of the items in the list is", total)

main()