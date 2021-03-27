def get_input_matrix():
    user_input = input().split()

    n = int(user_input[0])
    m = int(user_input[1])

    matrix = []

    for i in range(n):
        user_input_matrix = input().split()
        row = []
        for j in range(m):
            row.append(int(user_input_matrix[j]))
        matrix.append(row)
    
    return (matrix, n, m)

def prime_sieve(n):
    primes, sieve = {}, [True] * int(n + 1)

    for p in range(2, n + 1):
        if sieve[p]:
            primes[p] = p
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    return primes

matrix, n, m = get_input_matrix()
primes = prime_sieve(100100)

lesser_row_count = 999999

columns_count = [0] * m

for i in range(n):
    row_count = 0

    for j in range(m):
        while (not primes.get(matrix[i][j])):
            matrix[i][j] += 1
            row_count += 1
            columns_count[j] += 1

            if row_count >= lesser_row_count and columns_count[j] >= lesser_row_count:
                break

    lesser_row_count = min(row_count, lesser_row_count)

print(min(lesser_row_count, *columns_count))
