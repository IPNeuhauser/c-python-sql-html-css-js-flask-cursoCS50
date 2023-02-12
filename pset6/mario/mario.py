from cs50  import get_int

def main():
    while True:
        number = get_int("weight: ")
        if number > 0 and number < 9:
            break

    for x in range(number):
        print(" " * (number - 1 - x), end = "")
        print("#" * (x + 1), end = "")
        print()

main()