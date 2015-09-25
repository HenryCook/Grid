#!/usr/bin/python
import sys


# Create grid list
grid = []


def main():
    # Choose command
    command = raw_input("Select (I) to create a grid, (S) to display it, (C) to clear it and (X) to exit: ").upper()

    if command == "I":
        creategrid()
    elif command == "S":
        printgrid(grid)
    elif command == "C":
        cleargrid()
    elif command == "X":
        sys.exit()
    else:
        print "That does not match any of the available commands"

    while True:
        if grid > 0:
            main()
        else:
            break


def creategrid():
    # Input for rows and columns
    print "Enter the number of rows and columns"

    row = int(input("row: "))
    column = int(input("column: "))

    for n in range(row):
        grid.append(["O"] * column)


def cleargrid():
    # Clear grid
    print "Clearing grid"
    del grid[:]


def printgrid(grid):
    # Print grid
    print "Displaying grid"
    for row in grid:
        print " ".join(row)
    return

if __name__ == '__main__':
    main()
