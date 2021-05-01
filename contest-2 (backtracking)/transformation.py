def get_user_input():
    user_input = input().split()
    x = int(user_input[0])
    n = int(user_input[1])
    return x, n

def is_valid(x, n):
	return x <= n

results = []

def transformation(x, n, seq, i):
	if x == n:
		results.append((i, seq))
	else:
		value_append = (10 * x) + 1
		value_double = 2 * x
		if is_valid(value_append, n):
			transformation(value_append, n, [*seq, str(value_append)], i + 1)
		if is_valid(value_double, n):
			transformation(value_double, n, [*seq, str(value_double)], i + 1)

x, n = get_user_input()
transformation(x, n, [str(x)], 1)

if len(results) > 0:
	print("YES")
	for result in results:
		print(result[0])
		print(" ".join(result[1]))
else:
	print("NO")
