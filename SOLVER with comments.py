import numpy as np


def consec_rows():
    # goes through the rows of the grid, checks for 2 consecutive 1s or 0s, and places a 0 or 1 either side
    # the same number cannot appear in more than 2 consecutive squares.

    global changes  # tracks the number of changes we've made to the grid
    global changes1

    for row in range(10):
        for column in range(2, 10):

            if grid[row][column - 2] == x:
                if grid[row][column] == 0:
                    if grid[row][column] == grid[row][column - 1]:
                        grid[row][column - 2] = 1
                        changes += 1
                        changes1 += 1

                elif grid[row][column] == 1:
                    if grid[row][column] == grid[row][column - 1]:
                        grid[row][column - 2] = 0
                        changes += 1
                        changes1 += 1

        grid[row].reverse()  # i had to reverse the rows to make changes to the index 9, and 10 of each row

        for column in range(2, 10):

            if grid[row][column - 2] == x:
                if grid[row][column] == 0:
                    if grid[row][column] == grid[row][column - 1]:
                        grid[row][column - 2] = 1
                        changes += 1
                        changes1 += 1

                elif grid[row][column] == 1:
                    if grid[row][column] == grid[row][column - 1]:
                        grid[row][column - 2] = 0
                        changes += 1
                        changes1 += 1

        grid[row].reverse()  # and here the rows have to be reversed back again!


def get_columns():
    # this small function makes the columns into lists so their easier to work with
    global column_lists

    column_lists = []

    for column in range(0, 10):
        column_list = []
        for row in range(0, 10):
            cell = grid[row][column]
            column_list.append(cell)
        column_lists.append(column_list)


def consec_columns():
    # goes through the rows of the grid, checks for 2 consecutive 1s or 0s, and places a 0 or 1 either side
    # the same number cannot appear in more than 2 consecutive squares.

    global changes
    global changes1

    get_columns()  # calling the get_columns function described above
    for column in range(10):  # this is the exact same principle as the consec_rows function described above
        for row in range(2, 10):
            if column_lists[column][row] == 0:
                if column_lists[column][row] == column_lists[column][row - 1]:
                    if grid[row - 2][column] == x:
                        grid[row - 2][column] = 1
                        changes += 1
                        changes1 += 1

            elif column_lists[column][row] == 1:
                if column_lists[column][row] == column_lists[column][row - 1]:
                    if grid[row - 2][column] == x:
                        grid[row - 2][column] = 0
                        changes += 1
                        changes1 += 1

        column_lists[column].reverse()

        for row in range(2, 10):
            if column_lists[column][row] == 0:
                if column_lists[column][row] == column_lists[column][row - 1]:
                    if grid[10 - row + 1][column] == x:
                        grid[10 - row + 1][column] = 1
                        changes += 1
                        changes1 += 1

            elif column_lists[column][row] == 1:
                if column_lists[column][row] == column_lists[column][row - 1]:
                    if grid[10 - row + 1][column] == x:
                        grid[10 - row + 1][column] = 0
                        changes += 1
                        changes1 += 1


def consecutives():
    # this smashes the 2 functions into one
    consec_rows()
    consec_columns()


def iter_consecutives_0():
    # here we set the changes variable to 0 and call consecutives for the first time
    global changes
    changes = 0
    consecutives()


def iter_consecutives_1():
    # now we check if some changes were made (if changes > 0) and if there were, we call consecutives again
    while changes > 0:
        iter_consecutives_0()


def iter_consecutives():
    # this function triggers the iterative process outlined above
    iter_consecutives_0()
    iter_consecutives_1()


def gaps_rows():
    # here we check each row for a 1, blank, 1 pattern or 0, blank, 0 and place a 0 or 1 in the gap.
    # the same number cannot appear in more than two consecutive squares in any row or column.

    global changes
    global changes1

    for row in range(10):
        for column in range(1, 9):

            if grid[row][column] == x:
                if grid[row][column - 1] == 0:
                    if grid[row][column - 1] == grid[row][column + 1]:
                        grid[row][column] = 1
                        changes += 1
                        changes1 += 1

                elif grid[row][column - 1] == 1:
                    if grid[row][column - 1] == grid[row][column + 1]:
                        grid[row][column] = 0
                        changes += 1
                        changes1 += 1


def gaps_columns():
    # checks for, and then fills in, gaps in the columns

    global changes
    global changes1

    for column in range(10):
        for row in range(1, 9):

            if grid[row][column] == x:
                if grid[row - 1][column] == 0:
                    if grid[row - 1][column] == grid[row + 1][column]:
                        grid[row][column] = 1
                        changes += 1
                        changes1 += 1

                elif grid[row - 1][column] == 1:
                    if grid[row - 1][column] == grid[row + 1][column]:
                        grid[row][column] = 0
                        changes += 1
                        changes1 += 1


def gaps():
    # as before, with the consecutives function, smashes the rows and columns into one
    gaps_rows()
    gaps_columns()


def iter_gaps_0():
    # same iterative process as before
    global changes
    changes = 0
    gaps()


def iter_gaps_1():
    while changes > 0:
        iter_gaps_0()


def iter_gaps():
    iter_gaps_0()
    iter_gaps_1()


def check_rows():
    # checks if there's 5 0s in a row, and sets the remaining blanks to 1s, and v/v.
    global changes
    global changes1

    for row in range(10):
        for column in range(10):

            if grid[row].count(x) > 0:

                if grid[row].count(1) == 5:
                    grid_change = grid[row].index(x)
                    grid[row][grid_change] = 0
                    changes += 1
                    changes1 += 1

                elif grid[row].count(0) == 5:
                    grid_change = grid[row].index(x)
                    grid[row][grid_change] = 1
                    changes += 1
                    changes1 += 1


def check_columns():
    # checks if there's 5 0s in a column, and sets the remaining blanks to 1s, and v/v.
    global changes
    global changes1

    for column in range(10):
        column_list = []

        for row in range(10):
            row = grid[row][column]
            column_list.append(row)

        if column_list.count(x) > 0:

            if column_list.count(1) == 5:
                grid_change = column_list.index(x)
                grid[grid_change][column] = 0
                changes += 1
                changes1 += 1

            elif column_list.count(0) == 5:
                grid_change = column_list.index(x)
                grid[grid_change][column] = 1
                changes += 1
                changes1 += 1


def fives():
    # smashes the two above functions together
    check_rows()
    check_columns()


def iter_fives_0():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    global changes
    changes = 0
    fives()


def iter_fives_1():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    while changes > 0:
        iter_fives_0()


def iter_fives():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    iter_fives_0()
    iter_fives_1()


def fours_rows():
    # a more complicated function here.
    # this checks to see if there's 4 1s and 3 0s or v/v
    # if yes, checks for the given pattern

    global changes
    global changes1

    for row in range(10):

        if grid[row].count(0) == 4:
            if grid[row].count(1) == 3:
                if "'x', 'x', 'x', 1" in str(grid[row]):
                    for column in range(10):
                        if grid[row][column] == x:
                            grid[row][column] = 1
                            # in this instance, the first blank in the string, must be a 1
                            # if not, this would mean the two remaining 1s, fill the next 2 blanks
                            # this causes 3 1s in consecutive cells, which is not allowed
                            changes += 1
                            changes1 += 1
                            break

        elif grid[row].count(1) == 4:
            if grid[row].count(0) == 3:
                if "'x', 'x', 'x', 0" in str(grid[row]):
                    for column in range(10):
                        if grid[row][column] == x:
                            grid[row][column] = 0
                            changes += 1
                            changes1 += 1
                            break


def fours_columns():
    # same as above, just looking at columns now.
    global changes
    global changes1

    get_columns()
    for column in range(10):

        if column_lists[column].count(0) == 4:
            if column_lists[column].count(1) == 3:
                if "'x', 'x', 'x', 1" in str(column_lists[column]):
                    for row in range(10):
                        if grid[row][column] == x:
                            grid[row][column] = 1
                            changes += 1
                            changes1 += 1
                            break

        elif column_lists[column].count(1) == 4:
            if column_lists[column].count(0) == 3:
                if "'x', 'x', 'x', 0" in str(column_lists[column]):
                    for row in range(10):
                        if grid[row][column] == x:
                            grid[row][column] = 0
                            changes += 1
                            changes1 += 1
                            break


def fours():
    # rows, and columns into one
    fours_rows()
    fours_columns()


def iter_fours_0():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    global changes
    changes = 0
    fours()


def iter_fours_1():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    while changes > 0:
        iter_fours_0()


def iter_fours():
    # sets up the iterative process which repeats until no more changes are being made to the grid
    iter_fours_0()
    iter_fours_1()


def knowns():
    # here, this function, calls all the above iterative processes, one by one
    iter_consecutives()
    iter_gaps()
    iter_fives()
    iter_fours()


def iter_knowns_0():
    # this is what the changes1 variable is for.
    # it does not get reset, like changes does after each prior run of functions.
    # it only gets reset after the macro run of all the functions
    global changes1
    changes1 = 0
    knowns()


def iter_knowns_1():
    # we check if there were some changes made
    # if yes, we run the entire process again, until no more changes are made
    while changes1 > 0:
        iter_knowns_0()


def iter_knowns():
    iter_knowns_0()
    iter_knowns_1()


def check():
    # this simply checks the grid in its current state, and returns false, if any condition is violated

    get_columns()
    str_rows = str(grid)
    str_columns = str(column_lists)

    if "0, 0, 0" in str_rows:  # checking for 3 consecutive 0s or 1s, in rows, and columns
        return False
    elif "1, 1, 1" in str_rows:
        return False
    elif "0, 0, 0" in str_columns:
        return False
    elif "1, 1, 1" in str_columns:
        return False

    for rows in range(10):  # checks for more than 5 0s or more than 5 1s in any row/column
        if grid[rows].count(0) > 5:
            return False
        elif grid[rows].count(1) > 5:
            return False

    for columns in range(10):
        if column_lists[columns].count(0) > 5:
            return False
        elif column_lists[columns].count(1) > 5:
            return False

    for rows in range(10):  # checks that no two completed rows/columns are the same
        for rows1 in range(10):
            if rows != rows1:
                if grid[rows].count(x) == 0:
                    if grid[rows] == grid[rows1]:
                        return False

    for columns in range(10):
        for columns1 in range(10):
            if columns != columns1:
                if column_lists[columns].count(x) == 0:
                    if column_lists[columns] == column_lists[columns1]:
                        return False


def brute_force():
    # now we start trying numbers in the remaining blanks, filling out the grid, and backtracking if we find a problem
    for row in range(10):
        for column in range(10):  # search through the cells in the grid one by one

            if grid[row][column] == x:
                grid[row][column] = 0  # try a 0 when we find the first blank

                change_locations.append([row, column])
                # we append an empty list, with the location of the change we just made

                check()  # run the check function to see if the change fits the constraints

                if check() == False:
                    grid[row][column] = 1  # if we break the rules, we try a 1

                    check()  # we check again

                    if check() == False:
                        grid[row][column] = x  # if the rules are still broken, we revert the change to a blank

                        del change_locations[-1]
                        # then we delete the most recent entry in the change_locations list

                        another_check()  # then we call this function

                    else:
                        iter_knowns_2()
                        brute_force()
                else:
                    iter_knowns_2()
                    brute_force()


def iter_knowns_2():
    global grid

    #  this is a long-winded way of getting around a problem i faced when trying to 'save' a grid without it then...
    #  ...changing as the program made changes to the grid.

    grid_list_0 = []
    grid_list_1 = []
    grid_list_2 = []
    grid_list_3 = []
    grid_list_4 = []
    grid_list_5 = []
    grid_list_6 = []
    grid_list_7 = []
    grid_list_8 = []
    grid_list_9 = []

    grid_list = []

    for column in range(10):
        grid_list_0.append(grid[0][column])
    grid_list.append(grid_list_0)

    for column in range(10):
        grid_list_1.append(grid[1][column])
    grid_list.append(grid_list_1)

    for column in range(10):
        grid_list_2.append(grid[2][column])
    grid_list.append(grid_list_2)

    for column in range(10):
        grid_list_3.append(grid[3][column])
    grid_list.append(grid_list_3)

    for column in range(10):
        grid_list_4.append(grid[4][column])
    grid_list.append(grid_list_4)

    for column in range(10):
        grid_list_5.append(grid[5][column])
    grid_list.append(grid_list_5)

    for column in range(10):
        grid_list_6.append(grid[6][column])
    grid_list.append(grid_list_6)

    for column in range(10):
        grid_list_7.append(grid[7][column])
    grid_list.append(grid_list_7)

    for column in range(10):
        grid_list_8.append(grid[8][column])
    grid_list.append(grid_list_8)

    for column in range(10):
        grid_list_9.append(grid[9][column])
    grid_list.append(grid_list_9)

    grids_list.append(grid_list)
    # now the master grids_list is updated with the latest 'save' of the grid as the most recent item in the list

    iter_knowns()  # after making the change, we run iter_knowns to see if any other changes can be made to the grid

    check()

    if check() == False:  # we have a problem with the change we just made
        grid = grids_list[-1]  # grid is reverted to the last 'save'

        del grids_list[-1]  # last 'save' is now deleted from the master list

        if grid[change_locations[-1][0]][change_locations[-1][1]] == 0:
            grid[change_locations[-1][0]][change_locations[-1][1]] = 1

            # if the last change was a 0, we make it a 1 and go again

            check()

            if check() == False:
                grid[change_locations[-1][0]][change_locations[-1][1]] = x
                # change is reverted to a blank

                del change_locations[-1]  # delete the most recent entry in the change_locations list
                grid = grids_list[-1]  # grid is reverted to the most recent save

                del grids_list[-1]  # and this most recent save can now be deleted from the list

                another_check()  # now we call another_check to go alter the next most recent change we made

            else:
                iter_knowns_3()

        elif grid[change_locations[-1][0]][change_locations[-1][1]] == 1:
            grid[change_locations[-1][0]][change_locations[-1][1]] = x

        # if the last change was a 1, we revert it straight away.
        # this is because we prioritise 0s when checking, so if it's a 1, then we've already ruled out this being a 0...
        # ...because of some other problem.

            del change_locations[-1]  # deletes the most recent entry in the change_locations list
            grid = grids_list[-1]  # grid is reverted to the most recent save

            del grids_list[-1]  # this most recent save can now be deleted from the master list

            another_check()


def another_check():
    # we've arrived here after reverting our most recent change to a blank because of a problem.

    global grid

    if grid[change_locations[-1][0]][change_locations[-1][1]] == 0:
        grid[change_locations[-1][0]][change_locations[-1][1]] = 1

        # we change the next most recent change to a 1 if it was a 0 before.

        check()

        if check() == False:
            grid[change_locations[-1][0]][change_locations[-1][1]] = x
            # if that doesn't work, we revert it to an x

            del change_locations[-1]  # remove the last entry to change_locations
            grid = grids_list[-1]  # and revert the grid to its most recent 'saved' state

            del grids_list[-1]  # now delete that most recent 'save'

            another_check()  # and call this function again!

        else:
            iter_knowns_3()

    elif grid[change_locations[-1][0]][change_locations[-1][1]] == 1:
        grid[change_locations[-1][0]][change_locations[-1][1]] = x

        # if the next most recent change was a 1, we revert it straight away.
        # this is because we prioritise 0s when checking, so if it's a 1, then we've already ruled out this being a 0...
        # ...because of some other problem.

        del change_locations[-1]  # remove the last entry to change_locations
        grid = grids_list[-1]  # and revert the grid to its most recent 'saved' state

        del grids_list[-1]  # now delete that most recent 'save'

        another_check()  # and call this function again!


def iter_knowns_3():
    global grid

    grid_list_0 = []
    grid_list_1 = []
    grid_list_2 = []
    grid_list_3 = []
    grid_list_4 = []
    grid_list_5 = []
    grid_list_6 = []
    grid_list_7 = []
    grid_list_8 = []
    grid_list_9 = []

    grid_list = []

    for column in range(10):
        grid_list_0.append(grid[0][column])
    grid_list.append(grid_list_0)

    for column in range(10):
        grid_list_1.append(grid[1][column])
    grid_list.append(grid_list_1)

    for column in range(10):
        grid_list_2.append(grid[2][column])
    grid_list.append(grid_list_2)

    for column in range(10):
        grid_list_3.append(grid[3][column])
    grid_list.append(grid_list_3)

    for column in range(10):
        grid_list_4.append(grid[4][column])
    grid_list.append(grid_list_4)

    for column in range(10):
        grid_list_5.append(grid[5][column])
    grid_list.append(grid_list_5)

    for column in range(10):
        grid_list_6.append(grid[6][column])
    grid_list.append(grid_list_6)

    for column in range(10):
        grid_list_7.append(grid[7][column])
    grid_list.append(grid_list_7)

    for column in range(10):
        grid_list_8.append(grid[8][column])
    grid_list.append(grid_list_8)

    for column in range(10):
        grid_list_9.append(grid[9][column])
    grid_list.append(grid_list_9)

    grids_list.append(grid_list)

    # the above code saves the grid

    iter_knowns()  # iter_knowns to fill out the 'known' blanks after the change from 0 to 1 has been made

    check()

    if check() == False:
        grid = grids_list[-1]  # grid is reverted to the state before iter_knowns is called

        del grids_list[-1]  # most recent save is deleted

        grid[change_locations[-1][0]][change_locations[-1][1]] = x
        # the change reverts to a blank as the 0 was previously found out to be incorrect in iter_knowns_2

        del change_locations[-1]  # most recent change location removed from list
        grid = grids_list[-1]  # grid reverted back one step again

        del grids_list[-1]  # this save gets removed from the list

        another_check()  # this function is called to backtrack another step further!


def solve():
    # finally the solve function starts the entire process
    global grid

    grid = [[x, x, x, x, x, x, 1, x, x, x],  # this is where the start grid is input for the program to solve.
            [1, x, x, x, x, 1, x, 0, x, x],
            [1, 1, x, x, x, x, x, x, 1, x],
            [x, x, 0, x, x, x, x, 0, x, 0],
            [x, x, x, x, x, x, x, 1, x, x],
            [x, 0, x, x, x, 0, x, x, x, x],
            [1, x, x, x, 0, x, 1, x, 0, x],
            [0, 1, x, x, x, x, x, x, x, 1],
            [x, x, x, 0, 0, x, x, x, x, x],
            [x, x, x, x, 1, x, x, x, 0, 0]]

    print("START GRID:")
    print(np.matrix(grid), "\n")
    iter_knowns()  # step one is to fill out the known cells based on what we've been given by the start grid
    brute_force()
    # we move through each blank, trying a 0 first, and backtracking to make a change, after each check returns False
    print(np.matrix(grid))
    if check() != False:
        print("GRID COMPLETE")


x = 'x'  # makes it easier setting the variable x to the string 'x'
grids_list = []  # this is our master list of all the saved grids as we move through the recursive backtracking process
change_locations = []
# this is our master nested list of locations within the grid where we've made a change. helpful when it comes to...
# ...reverting that change

solve()
