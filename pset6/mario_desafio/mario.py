from cs50 import get_int

def main():
    while True:
        number = get_int("Height: ")
        if number > 0 and number < 9:
            break

    for x in range(number):
        print(" " * (number - x - 1), end = "")
        print("#" * (x+1), end = "")
        print("  ", end = "")
        print("#" * (x+1),end = "")
        print()

main()