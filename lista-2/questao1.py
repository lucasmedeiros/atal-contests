def get_user_input():
	txt = input()
	m = int(input())
	return txt, m

def blank_space_counter(s, m):
	idx = -1
	l = len(s)
	i = 0
	while i <= (l - m) and idx == -1:
		j = 0
		while j < m and s[i + j] == " ":
			j += 1
		if j == m:
			idx = i
		i += max(1, j)
	return idx

def main():
	txt, m = get_user_input()
	idx = blank_space_counter(txt, m)

	print("Vazio" if idx == -1 else idx)

main()
