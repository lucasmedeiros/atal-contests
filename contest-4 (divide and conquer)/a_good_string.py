def get_cost(l, r, c, s):
	cnt = 0
	for i in range(l, r + 1):
		if (s[i] != c):
			cnt += 1
	return cnt

def get_min(l, r, c, s):
	if l == r:
		return 0 if s[l] == c else 1
	
	mid = int((l + r) / 2)
	nc = chr(ord(c) + 1)

	return min(get_cost(l, mid, c, s) + get_min(mid + 1, r, nc, s), get_cost(mid + 1, r, c, s) + get_min(l, mid, nc, s))

def main():
	t = int(input())
	s = 'a' * 140000
	c = 'a'

	for x in range(t):
		n = int(input())
		s = input()

		print(get_min(0, n - 1, c, s))
main()