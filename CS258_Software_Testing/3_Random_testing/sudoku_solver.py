# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# TODO
impossible = []
# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
# hard = [[1,0,0,0,0,7,0,9,0],
#         [0,3,0,0,2,0,0,0,8],
#         [0,0,9,6,0,0,5,0,0],
#         [0,0,5,3,0,0,9,0,0],
#         [0,1,0,0,8,0,0,0,2],
#         [6,0,0,0,0,4,0,0,0],
#         [3,0,0,0,0,0,0,1,0],
#         [0,4,0,0,0,0,0,0,7],
#         [0,0,7,0,0,0,3,0,0]]

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

def get_row(grid, row_index):
	return grid[row_index]

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

def get_blanks (grid):
	blanks = []
	for x in range(9):
		for y in range(9):
			if grid[x][y] == 0:
				blanks.append({
							"x": x,
							"y": y,
							"guesses": make_rep(),
							"guessed": make_rep() 
						})
	return blanks

def set_valid_guesses (blanks, grid, offset_index = 0):
	length = len(blanks)
	index = offset_index
	print "start at index " + str(index)
	while (index < length):
		blank = blanks[index]
		rep = make_rep()
		has_possible_guess = False
		for num in get_row(grid, blank["x"]):
			if num == 0:
				continue
			rep[num] = True
		for num in get_column(grid, blank["y"]):
			if num == 0:
				continue
			rep[num] = True
		for num in get_box(grid, blank["x"] / 3, blank["x"] / 3):
			if num == 0:
				continue
			rep[num] = True
		# make sure at least one is open (False)
		for guess in rep:
			if (rep[guess] == False):
				has_possible_guess = True
				break
		if has_possible_guess:
			blank["guesses"] = rep 
			index += 1
		else:
			print "bail at index " + str(index)
			return False

	# valid guesses for all blanks
	print "all valid guesses, index hit " + str(index)
	return True


def fill_blanks (blanks, grid):
	length = len(blanks)
	index = 0
	while (index < length):
		blank = blanks[index]

		did_fill = False
		#print str(blank["x"]) + "," + str(blank["y"])
		for guess in blank["guesses"]:
			#print "idx: " + str(index) + ", " + str(guess) + ":" + str(blank["guesses"][guess])
			if (blank["guesses"][guess] == False and not blank["guessed"][guess]):
				grid[blank["x"]][blank["y"]] = guess
				blank["guessed"][guess] = True
				did_fill = True
				print "set blank " + str(index) + " to " + str(guess)
				break

		if (index == 0 and did_fill != True):
			# nothing will work
			print "fail"
			return False
		if (did_fill == True and set_valid_guesses(blanks, grid, index+1)):
			index += 1
		else:
			print "backtrack from " + str(index)
			last_blank = blanks[index-1]
			# set to zero and backtrack
			grid[blank["x"]][blank["y"]] = "X"
			print print_grid(grid)
			grid[blank["x"]][blank["y"]] = 0
			blank["last_blank"] = 0
			grid[last_blank["x"]][last_blank["y"]] = 0
			index -= 1
			set_valid_guesses(blanks, grid, index)

	return check_sudoku(grid)


def print_grid (grid):
	grid_str = "\n"
	for x in range(9):
		line_str = ""
		if x != 0 and x % 3 == 0:
			line_str += "\n"
		for y in range(9):
			if y != 0 and y % 3 == 0:
				line_str += " "
			line_str += str(grid[x][y]) + " "
		grid_str += (line_str + "\n")

	return grid_str + "\n"

def solve_sudoku (grid):
    ###Your code here.
	is_valid = check_sudoku(grid)
	if (is_valid == True):
		blanks = get_blanks(grid)
		if (set_valid_guesses(blanks, grid)):
			fill_blanks(blanks, grid)
		return print_grid(grid)
		
	else:
		return is_valid

print "ill_formed: " + str(solve_sudoku(ill_formed)) # --> None
print "valid: " + str(solve_sudoku(valid))      # --> True
print "invalid: " + str(solve_sudoku(invalid))    # --> False
print "easy: " + str(solve_sudoku(easy))       # --> True
#print solve_sudoku(hard)       # --> True
