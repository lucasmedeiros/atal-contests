def get_user_input():
	size = int(input())
	elements = [0] * size

	for i in range(size):
		elements[i] = int(input())
	
	return size, elements

def get_lesser_number(x, candidates):
	if x < 10:
		return x
	
	if x > 45:
		return -1

	if x == 45:
		return 123456789
	
	index = 0
	base10 = 1
	solution = 0
	aux = x

	while aux > 0:
		number = candidates[index]

		if aux - number >= 0:
			aux -= number
			solution += number * base10
		else:
			solution += aux * base10
			aux = 0
		
		base10 *= 10

		index += 1
	
	return solution

size, elements = get_user_input()
candidates = list(range(9, 0, -1))

for i in range(size):
	print(get_lesser_number(elements[i], candidates))
