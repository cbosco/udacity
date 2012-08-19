# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Write a random tester for the Queue class.
def test_enqueue(q, l, max_size, some_random_input):
	was_full = q.full()
	assert was_full == (max_size == len(l))
	print "was full? " + str(was_full) + "; enqueued " + str(some_random_input)
	success = q.enqueue(some_random_input)
	if not was_full:
		assert success
		l.append(some_random_input)

def test_dequeue(q, l):
	was_empty = q.empty()
	assert was_empty == (0 == len(l))
	some_random_output = q.dequeue()
	if not was_empty:
		assert some_random_output != None
		assert l.pop(0) == some_random_output
		#print "asserted " + str(some_random_output) + " was same"

def test():
	# not random
	# Note -- this assignment did not pass until I added enough random tests
	#		  (that was it)
	MAX_SIZE = 50000
	l = []
	q = Queue(MAX_SIZE)
	max_signed_int = 2147483647

	for number in range(2 * MAX_SIZE):
		some_random_input = int(random.random() * max_signed_int)
		# randomly choose enqueue, dequeue 
		# (independent of some_some_random_input)
		if (random.random() < 0.5):
			# enqueues with bounds special cases
			if (random.random() < 0.4):
				# positive random int
				test_enqueue(q, l, MAX_SIZE, some_random_input)
			elif (random.random() < 0.45):
				# special case for enqueue 0
				test_enqueue(q, l, MAX_SIZE, 0)
			elif (random.random() < 0.5):
				# special case for enqueue max bound
				test_enqueue(q, l, MAX_SIZE, max_signed_int)
			elif (random.random() < 0.55):
				# special case for enqueue min bound
				test_enqueue(q, l, MAX_SIZE, -1 * max_signed_int)
			else:
				# negative random int
				test_enqueue(q, l, MAX_SIZE, -1 * some_random_input)
		else:
			test_dequeue(q, l)
		q.checkRep()

test()
