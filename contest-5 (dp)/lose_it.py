def get_minimum_removals(n, seq, base, dic):
	for i in range(n):
		elem = seq[i]

		if (dic[elem] == 0) or (base[dic[elem] - 1] > base[dic[elem]]):
			base[dic[elem]] += 1

	return n - 6 * base[5]

n = int(input())
seq = [int(x) for x in input().split()]
base = [0] * 6
dic = {
	4: 0,
	8: 1,
	15: 2,
	16: 3,
	23: 4,
	42: 5
}
print(get_minimum_removals(n, seq, base, dic))