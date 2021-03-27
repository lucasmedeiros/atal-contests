def get_user_input():
    user_input = input().split()
    k = int(user_input[0])
    r = int(user_input[1])
    return k, r

def get_min_shovels(k, r):
    unlimited_coins = 10

    for i in range(1, unlimited_coins + 1):
        value = k * i

        if value % unlimited_coins == 0 or value % unlimited_coins == r:
            return i

k, r = get_user_input()
print(get_min_shovels(k, r))
