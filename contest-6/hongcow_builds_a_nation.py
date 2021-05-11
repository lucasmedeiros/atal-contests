n, m, k = [int(x) for x in input().split()]
special = [int(x) for x in input().split()]

root = list(range(n + 1))

def par(p):
	if root[p] != p:
		root[p] = par(root[p])
	return root[p]

def c2(n):
	return n * (n - 1) / 2

for i in range(m):
	u, v = map(par, [int(x) for x in input().split()])
	root[v] = u

s = [0] * (n + 1)
for i in range(n+1):
	s[par(i)] += 1

left = n
maximum_edges = 0
biggest = 0

for x in special:
  d = par(x)

  if s[d] > biggest:
    biggest = s[d]

  maximum_edges += c2(s[d])
  left -= s[d]

maximum_edges -= c2(biggest)
maximum_edges += c2(biggest + left)
maximum_edges -= m

print(int(maximum_edges))
