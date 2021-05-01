def get_maximum_points(n, cnt):
	if n == 0:
		return 0
	
	if n == 1:
		return cnt[1]
	
	maximum = 0

n = int(input())
MAX = 100100
cnt = [0] * MAX

line = input().split()
for i in range(n):
	elem = int(line[i])
	cnt[elem] += 1

dp = [0] * MAX

dp[0] = 0
dp[1] = cnt[1]

for i in range(2, MAX):
	dp[i] = max(dp[i - 1], dp[i - 2] + cnt[i] * i)

print(dp[MAX - 1])
