# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    ###Your code here.

	# a big input
	# (Queue impl #1 bug)
	q = Queue(1)
	succeeded = q.enqueue(10000000)
	assert(succeeded == True)
	value = q.dequeue()
	assert(value == 10000000)

	# Queue of length 3
	q = Queue(3)
	is_empty = q.empty()
	is_full = q.full()
	assert(is_empty == True)
	assert(is_full == False)
	# Up...
	succeeded = q.enqueue(10)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == False)
	succeeded = q.enqueue(20)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == False)
	succeeded = q.enqueue(30)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == True)
	succeeded = q.enqueue(40)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == False)
	assert(is_empty == False)
	assert(is_full == True)

	# Down...
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 10)
	assert(is_empty == False)
	assert(is_full == False)
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 20)
	assert(is_empty == False)
	assert(is_full == False)
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 30)
	assert(is_empty == True)
	assert(is_full == False)
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == None)
	assert(is_empty == True)
	assert(is_full == False)

	# Up again...
	succeeded = q.enqueue(10)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == False)
	succeeded = q.enqueue(20)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == False)
	succeeded = q.enqueue(30)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == True)

	# Down again
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 10)
	assert(is_empty == False)
	assert(is_full == False)

	# Up again...
	succeeded = q.enqueue(40)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == True)

	# Down again
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 20)
	assert(is_empty == False)
	assert(is_full == False)
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 30)
	assert(is_empty == False)
	assert(is_full == False)

	# Up again...
	succeeded = q.enqueue(100)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == False)

	# Down again
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 40)
	assert(is_empty == False)
	assert(is_full == False)
	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 100)
	assert(is_empty == True)
	assert(is_full == False)

	# big queue
	max_size = 100
	q = Queue(max_size)
	is_empty = q.empty()
	is_full = q.full()
	assert(is_empty == True)
	assert(is_full == False)
	for i in range(0,max_size - 1):
		succeeded = q.enqueue(i)
		is_empty = q.empty()
		is_full = q.full()
		assert(succeeded == True)
		assert(is_empty == False)
		assert(is_full == False)

	succeeded = q.enqueue(100)
	is_empty = q.empty()
	is_full = q.full()
	assert(succeeded == True)
	assert(is_empty == False)
	assert(is_full == True)

	# beyond maximum, stress test... (nothing)
	for i in range(0, max_size):
		succeeded = q.enqueue(i)
		is_empty = q.empty()
		is_full = q.full()
		assert(succeeded == False)
		assert(is_empty == False)
		assert(is_full == True)

	for i in range(0, max_size - 1):
		value = q.dequeue()
		is_empty = q.empty()
		is_full = q.full()
		assert(value == i)
		assert(is_full == False)
		assert(is_empty == False)

	value = q.dequeue()
	is_empty = q.empty()
	is_full = q.full()
	assert(value == 100)
	assert(is_full == False)
	assert(is_empty == True)


	# beyond minimum, stress test... (nothing)
	for i in range(0, max_size):
		value = q.dequeue()
		is_full = q.full()
		is_empty = q.empty()
		assert(value == None)
		assert(is_empty == True)
		assert(is_full == False)


