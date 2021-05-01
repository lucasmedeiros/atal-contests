def binomial(n, k):
	if (k == 1 or k == n):
		return 1

	return binomial(n - 1, k) + binomial(n - 1, k - 1)

n, k = [int(x) for x in input().split()]

print(binomial(n, k))
