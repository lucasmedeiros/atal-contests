def get_user_input_days():
	return int(input())

def get_user_input_price():
	line_split = input().split()
	kg = int(line_split[0])
	price = int(line_split[1])
	return kg, price

def get_minimum_price():
	days = get_user_input_days()
	lowest_price = 100
	total = 0

	for i in range(days):
		kg, price = get_user_input_price()

		if price < lowest_price:
			lowest_price = price
		
		total += lowest_price * kg
	
	return total


print(get_minimum_price())