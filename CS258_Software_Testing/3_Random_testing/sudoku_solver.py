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


# This is just a backtrack of valid,
# above
very_easy = [[0,0,0,0,0,0,0,0,2],
			 [0,0,0,1,9,5,3,4,0],
			 [0,0,0,3,4,0,0,0,7],
			 [8,5,0,0,0,0,4,0,0],
			 [0,2,6,8,5,3,7,9,1],
			 [7,1,3,9,2,4,8,5,6],
			 [0,0,0,0,0,0,0,0,0],
			 [2,8,0,4,1,9,0,0,0],
			 [3,0,0,2,8,6,0,0,0]]

blank =	[[0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0]]

impossible = []
# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
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
	for row_index in range(row * 3, (row * 3)+3):
		for col_index in range(col * 3, (col * 3)+3):
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

# Sets rep with possible guesses, and true
# If there is only one guess, returns that guess
# If no possible guesses, returns false
def set_valid_guesses_for_blank (grid, blank):
	rep = blank["guesses"] = make_rep()
	has_possible_guess = False
	the_one_possible_guess = 0
	for num in get_row(grid, blank["row"]):
		if num == 0:
			continue
		rep[num] = True
	for num in get_column(grid, blank["column"]):
		if num == 0:
			continue
		rep[num] = True

	for num in get_box(grid, blank["row"] / 3, blank["column"] / 3):
		if num == 0:
			continue
		rep[num] = True

	for guess in rep:
		if (rep[guess] == False):
			if has_possible_guess:
				# at least 2 possibilities
				the_one_possible_guess = 0
				break
			else:
				the_one_possible_guess = guess
			has_possible_guess = True

	if the_one_possible_guess != 0:
		return the_one_possible_guess
	elif has_possible_guess:
		return True
	else:
		return False


def get_blanks (grid):
	blanks = []
	for row in range(9):
		for col in range(9):
			if grid[row][col] == 0:
				blank = {
							"row": row,
							"column": col,
							"guesses": make_rep(),
							"guessed": make_rep() 
						}

				guess = set_valid_guesses_for_blank( grid, blank )

				if guess == True:
					blanks.append( blank )
				elif guess == False:
					# this is a problem...
					print "should not happen.. invalid"
					grid[row][col] = "X"
					print print_grid(grid)
				else:
					# only one solution so fill it in
					grid[row][col] = guess
	return blanks

def set_valid_guesses (blanks, grid, offset_index = 0):
	length = len(blanks)
	index = offset_index
	#print "set valid guesses from index " + str(index)
	while (index < length):
		blank = blanks[index]
		guess = set_valid_guesses_for_blank( grid, blank )
		if guess == False:
			#print "bail at index " + str(index)
			return index
		else:
			index += 1


	# valid guesses for all blanks
	return True


def fill_blanks (grid, blanks):
	tries = 0	# debug/metrics
	length = len(blanks)
	index = 0
	while (index < length):
		tries += 1
		blank = blanks[index]

		did_fill = False

		#print print_guesses_and_guessed( blank )
		for guess in blank["guesses"]:
			if (blank["guesses"][guess] == False and not blank["guessed"][guess]):
				grid[blank["row"]][blank["column"]] = guess
				blank["guessed"][guess] = True
				did_fill = True
				#print "[" + str(blank["row"]) + "," + str(blank["column"]) + "] - set to " + str(guess)
				break

		if (index == 0 and did_fill != True):
			# nothing will work
			print "failed at " + str(tries) + " tries"
			return False

		if (did_fill == True):
			valid_or_bad_index = set_valid_guesses(blanks, grid, index + 1)
			if (valid_or_bad_index == True):
				index += 1
				continue

			elif (valid_or_bad_index > index):
				#print "ok, bailed at future index"
				# index stays the same, try this one again
				blanks[valid_or_bad_index]["guessed"] = make_rep()
				continue

		#print "backtrack from " + str(index)
		last_blank = blanks[index-1]
		# print/debug with printed grid and an X
		#grid[blank["row"]][blank["column"]] = "X"
		#print print_grid(grid)
		# reset to zero and backtrack
		grid[blank["row"]][blank["column"]] = 0
		# reset guesses for this blank
		blank["guessed"] = make_rep()
		index -= 1

	return tries

# debug print method
def print_guesses_and_guessed (blank):
	guesses_str = ""
	for guess in blank["guesses"]:
		if (blank["guesses"][guess] == False):
			guesses_str += str(guess) + ","
	guessed_str = ""
	for guess in blank["guessed"]:
		if (blank["guessed"][guess] == True):
			guessed_str += str(guess) + ","
	return "[" + str(blank["row"]) + "," + str(blank["column"]) + "] - guessed: [" + guessed_str + "] / [" + guesses_str + "]"

# debug print method
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
	tries = 0
	is_valid = check_sudoku(grid)
	if (is_valid == True):
		blanks = get_blanks(grid)
		if (set_valid_guesses(blanks, grid) == True):
			tries = fill_blanks(grid, blanks)
		return "(" + str(tries) + " tries)\n" + print_grid(grid)
		
	else:
		return is_valid

# row test: one possibility
assert set_valid_guesses_for_blank(
		[[0,1,2,3,4,5,6,8,9],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]],
		{
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == 7
# row test: no possibilities
assert set_valid_guesses_for_blank(
		[[0,1,2,3,4,5,6,8,9],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [7,0,0,0,0,0,0,0,0]],
		{
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == False
# row test: multiple possibilities
row_test_blank = {
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}
assert set_valid_guesses_for_blank(
		[[0,1,2,3,0,5,6,8,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]], 
		row_test_blank) == True
assert row_test_blank["guesses"] == {
			1: True,
			2: True,
			3: True,
			4: False,
			5: True,
			6: True,
			7: False,
			8: True,
			9: False
		}

# column test: one possibility
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0],
         [3,0,0,0,0,0,0,0,0],
         [4,0,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,0,0],
         [6,0,0,0,0,0,0,0,0],
         [8,0,0,0,0,0,0,0,0],
         [9,0,0,0,0,0,0,0,0]],
		{
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == 7
# column test: no possibilities
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,0,7],
         [1,0,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0],
         [3,0,0,0,0,0,0,0,0],
         [4,0,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,0,0],
         [6,0,0,0,0,0,0,0,0],
         [8,0,0,0,0,0,0,0,0],
         [9,0,0,0,0,0,0,0,0]],
		{
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == False
# row test: multiple possibilities
column_test_blank = {
			"row": 0,
			"column": 0,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0],
         [3,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [5,0,0,0,0,0,0,0,0],
         [6,0,0,0,0,0,0,0,0],
         [8,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]],
		column_test_blank) == True
assert column_test_blank["guesses"] == {
			1: True,
			2: True,
			3: True,
			4: False,
			5: True,
			6: True,
			7: False,
			8: True,
			9: False
		}

# box test: one possibility
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,1,2],
         [0,0,0,0,0,0,3,4,5],
         [0,0,0,0,0,0,6,8,9],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]],
		{
			"row": 0,
			"column": 6,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == 7
# box test: no possibilities
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,1,2],
         [0,0,0,0,0,0,3,4,5],
         [0,0,0,0,0,0,6,8,9],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,7,0,0]],
		{
			"row": 0,
			"column": 6,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}) == False
# row test: multiple possibilities
box_test_blank = {
			"row": 0,
			"column": 6,
			"guesses": make_rep(),
			"guessed": make_rep() 
		}
assert set_valid_guesses_for_blank(
        [[0,0,0,0,0,0,0,1,2],
         [0,0,0,0,0,0,3,0,5],
         [0,0,0,0,0,0,6,8,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]],
		box_test_blank) == True
assert box_test_blank["guesses"] == {
			1: True,
			2: True,
			3: True,
			4: False,
			5: True,
			6: True,
			7: False,
			8: True,
			9: False
		}

# run solver

print "\n"
print "ill_formed: " + str(solve_sudoku(ill_formed)) # --> None
print "\n"
print "valid: " + str(solve_sudoku(valid))      # --> grid
print "\n"
print "invalid: " + str(solve_sudoku(invalid))    # --> False
print "\n"
print "very_easy: " + str(solve_sudoku(very_easy))       # --> grid
print "\n"
print "blank: " + str(solve_sudoku(blank))       # --> grid
print "\n"
print "easy: " + str(solve_sudoku(easy))       # --> grid
print "\n"
print "hard:" + str(solve_sudoku(hard))       # --> grid
print "\n"
print "impossible:" + str(solve_sudoku(impossible))       # --> grid?
