def main():

    number = 3
    previous_number = 1
    total = 1

    while number > 1:
        previous_number = number
        number -= 1
        total *= previous_number * number
        number -= 1

    if total == 0:
        print(1)
    elif number < 0:
        print("Error")
    else:
        print(total)

main()