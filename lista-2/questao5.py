def get_user_input():
	d = int(input())
	return d

def encode(d):
	if (d == 1 or d == 0):
		return str(d)

	d1 = int(d / 2)
	d2 = d % 2
	d3 = int(d / 2)

	return encode(d1) + encode(d2) + encode(d3)


def main():
	d = get_user_input()
	print(encode(d))

main()
