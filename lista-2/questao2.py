def get_user_input():
	line = input().split()
	n = int(line[0])
	d = int(line[1])
	return n, d

def get_base_10(n):
	b = 1

	while int(n / b) > 9:
		b *= 10
	
	return b

def erase_numbers(n, d):
	b = get_base_10(n)
	aux = n
	aux_b = b
	c = 0

	while d > 0:
		div = int(aux / aux_b)
		if div == c:
			d -= 1
			new_b = int(b / 10)
			aux_new_b = new_b
			new_n = 0

			aux_b2 = b
			aux2 = n

			while aux_b2 > 0:
				div2 = int(aux2 / aux_b2)

				if (aux_b2 != aux_b):
					new_n += div2 * aux_new_b
					aux_new_b = int(aux_new_b / 10)
				
				aux2  = aux2 - (aux_b2 * div2)
				aux_b2 = int(aux_b2 / 10)
			
			if (aux_b == 1):
				c += 1
			
			b = new_b
			n = new_n
			aux = n
			aux_b = b
		else:
			aux -= (aux_b * div)
			aux_b = int(aux_b / 10)

			if (aux_b == 0):
				c += 1
				aux_b = b
				aux = n
		
	return n


n, d = get_user_input()
print(erase_numbers(n, d))
