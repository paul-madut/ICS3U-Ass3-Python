#!/usr/bin//env python3

# Created by: Paul Madut
# Created on: October 2019
# This is the a program used to calculate area/perimter of a rectangle


def main():
    # This functions compares 2 numbers
    print("The program compares two numbers")
    print("")

    # Input
    integer_1 = float(input("Enter a number: "))
    integer_2 = float(input("Enter a second number: "))
    # Process
    if integer_1 == integer_2:
        print("These two numbers are equal.")
    elif integer_1 > integer_2:
        print("{} is the larger of the two numbers".format(integer_1))
    elif integer_1 < integer_2:
        print("{} is the larger of the two numbers".format(integer_2))
    else:
        print("Please enter a valid response")


if __name__ == "__main__":
    main()
