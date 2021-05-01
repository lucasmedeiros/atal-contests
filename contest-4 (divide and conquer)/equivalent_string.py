def get_user_input():
	a = input()
	b = input()
	return a, b

def equivalent(a, b, n):
	if a == b:
		return True

	if (n & 1):
		return False
	
	if (n == 1):
		return False

	n = int(n / 2)

	a1 = a[:n]
	a2 = a[n:]

	b1 = b[:n]
	b2 = b[n:]

	return (equivalent(a1, b2, n) and equivalent(a2, b1, n)) or (equivalent(a1, b1, n) and equivalent(a2, b2, n))

a, b = get_user_input()
n = len(a)
if equivalent(a, b, n):
	print("YES")
else:
	print("NO")
