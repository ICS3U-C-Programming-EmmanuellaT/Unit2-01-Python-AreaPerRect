#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# This program asks the length and the width of
# a rectangle, calculates the area and perimeter
# back to the user with proper units.
def main():
    # get the length from the user and convert to an integer
    length = int(input("Enter length of the rectangle (cm): "))

    # get the width from the user and convert to an integer
    width = int(input("Enter width of the rectangle (cm): "))

    # calculate the area and perimeter of a rectangle
    Area = length * width
    perimeter = 2 * (length + width)

    # display the area and perimeter to the user with proper units
    print("The area is: {}cm²".format(Area))
    print("The perimeter is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()
