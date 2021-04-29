def get_user_input():
	s = [int(x) for x in input().split()]
	return s

def is_perfect(a):
	size = len(a)
	for i in range(size - 1):
		number = a[i]
		next_number = a[i + 1]
		
		half = int(next_number / 2)
		triple = next_number * 3

		if number != half and number != triple:
			return False

	return True

def get_permutations(a, size):
	if size == 1:
		if is_perfect(a):
			print(" ".join(str(x) for x in a))
			exit(0)
 
	for i in range(size):
		get_permutations(a, size-1)
		if size % 2 == 1:
			a[0], a[size-1] = a[size-1], a[0]
		else:
			a[i], a[size-1] = a[size-1], a[i]

s = get_user_input()
get_permutations(s, len(s))
