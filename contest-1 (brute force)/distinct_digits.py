def get_user_input():
    user_input = input().split()
    num_a = int(user_input[0])
    num_b = int(user_input[1])
    return num_a, num_b

def get_unique_number_between(num_a, num_b):
    for i in range (num_a, num_b + 1):
        aux = i
        visited = [False] * 10

        while (aux):
            if visited[aux % 10]:
                break

            visited[aux % 10] = True
            aux = (int)(aux / 10)

        if aux == 0:
            return i
    else:
        return -1

num_a, num_b = get_user_input()

print(get_unique_number_between(num_a, num_b))
