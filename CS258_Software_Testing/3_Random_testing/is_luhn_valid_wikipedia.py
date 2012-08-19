# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def is_luhn_valid(n):
    ###Your code here.
	assert n
	n = str(n)
	sum_of_number = 0
	current_index = 0
	length_is_odd = len(n) % 2
	for i in n:
		current_index += 1
		if length_is_odd and not (current_index % 2):
			to_add = int(i) * 2
			to_add = (to_add - 9) if (to_add > 9) else to_add
			sum_of_number += to_add
		elif not length_is_odd and (current_index % 2):
			to_add = int(i) * 2
			to_add = (to_add - 9) if (to_add > 9) else to_add
			sum_of_number += to_add
		else:
			sum_of_number += int(i)
	
	if (sum_of_number % 10 == 0):
		print n + " passed"
		pass
	else:
		print n + " failed"

if __name__ == "__main__":
	is_luhn_valid(79927398710)
	is_luhn_valid(79927398711)
	is_luhn_valid(79927398712)
	is_luhn_valid(79927398713)
	is_luhn_valid(79927398714)
	is_luhn_valid(79927398715)
	is_luhn_valid(79927398716)
	is_luhn_valid(79927398717)
	is_luhn_valid(79927398718)
	is_luhn_valid(79927398719)
