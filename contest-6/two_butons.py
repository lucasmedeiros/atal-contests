n, m = [int(x) for x in input().split()]
count = 0

while m > n:
  if m % 2 == 0:
    m = int(m / 2)
  else:
    m += 1
  
  count += 1

print(count + abs(n - m))
