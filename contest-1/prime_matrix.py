def is_prime(n):
    if (n <= 1):
        return False

    if (n <= 3):
        return True
    
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    for i in range(5, int(n / 2)):
        if ((n % i) == 0):
            return False

    return True

user_input = input().split()

n = int(user_input[0])
m = int(user_input[1])

lesser_row_count = 999999
lesser_column_count = 999999

matrix = []

for i in range(n):
    user_input_matrix = input().split()
    row = []
    for j in range(m):
        row.append(int(user_input_matrix[j]))
    matrix.append(row)

times_incremented_matrix = []

for i in range(n):
    row = []
    row_count = 0

    for j in range(m):
        times_incremented = 0
        value = matrix[i][j]

        while (not is_prime(value)):
            value += 1
            times_incremented += 1

        row_count += times_incremented
        row.append(times_incremented)
    
    lesser_row_count = min(row_count, lesser_row_count)
    times_incremented_matrix.append(row)

if lesser_row_count > 0:
    for j in range(m):
        column_count = 0
        for i in range(n):
            column_count += times_incremented_matrix[i][j]

        lesser_column_count = min(column_count, lesser_column_count)

        if column_count == 0:
            break

print(min(lesser_row_count, lesser_column_count))
