# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

def make_rep():
	return {
		1: False,
		2: False,
		3: False,
		4: False,
		5: False,
		6: False,
		7: False,
		8: False,
		9: False,
	}

def get_column(grid, column_index):
	column = []
	for row_index in range(9):
		column.append(grid[row_index][column_index])

	return column

# row 1..3
# col 1..3
def get_box(grid, row, col):
	box = []
	for row_index in range(row * 3, (row * 3)+2):
		for col_index in range(col * 3, (col * 3)+2):
			box.append(grid[row_index][col_index])
	
	return box

def check_set_for_uniqueness(num_set):
	is_valid = True
	rep = make_rep()
	for num in num_set:
		# already set / duplicate
		if num != 0 and rep[num]:
			is_valid = False
			break
		rep[num] = True

	return is_valid

def check_sudoku(grid):
    ###Your code here.
	# sanity checking...
	# - is a 9x9 list of lists
	is_valid = None
	if len(grid) != 9:
		return is_valid
	for line in grid:
		if len(line) != 9:
			return is_valid
		# - contains, in each of its 81 elements, an integer in the range 0..9
		for num in line:
			if not isinstance( num, int ):
				return is_valid
			if not 0 <= num <= 9:
				return is_valid

	
	# legal game checks...
	is_valid = False
	# - each number in the range 1..9 occurs only once in each row 
	for line in grid:
		if not check_set_for_uniqueness(line):
			return is_valid

	# - each number in the range 1..9 occurs only once in each column
	for column_index in range(9):
		# create column
		column = get_column(grid, column_index)
		if not check_set_for_uniqueness(column):
			return is_valid

	# - each number the range 1..9 occurs only once in each of the nine
	#   3x3 sub-grids, or "boxes", that make up the board
	for row_index in range(3):
		for col_index in range(3):
			box = get_box(grid, row_index, col_index)
			if not check_set_for_uniqueness(box):
				return is_valid
	# yay!
	is_valid = True
	return is_valid

print check_sudoku(ill_formed) # --> None
print check_sudoku(valid)      # --> True
print check_sudoku(invalid)    # --> False
print check_sudoku(easy)       # --> True
print check_sudoku(hard)       # --> True


