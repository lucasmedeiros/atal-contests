def dfs(l, r, cur, arr, d):
	mx = 0
	mxi = 0

	for i in range(l, r + 1):
		if mx < arr[i]:
			mx = arr[i]
			mxi = i
		
	d[mxi] = cur

	if mxi > l:
		dfs(l, mxi - 1, cur + 1, arr, d)
	
	if mxi < r:
		dfs(mxi + 1, r, cur + 1, arr, d)

def main():
	t = int(input())
	arr = [0] * 110
	d = [0] * 110

	for x in range(t):
		n = int(input())
		line = input().split()
		arr = [int(i) for i in line]
		dfs(0, n - 1, 0, arr, d)
		for i in range(n):
			print(d[i], end=" ")
main()