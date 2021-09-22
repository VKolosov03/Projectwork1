import sys

def main_input():
#main_input()-get value of capacity and amount of bars

	capacity = input("Capacity of bag: ")
	bars_amount = input("Number of different bars: ")
	if not (capacity.isdigit() and bars_amount.isdigit()):
#isdigit()-check elements for digits

		print("You can't write in this way!Try again!")
		main_input()
		sys.exit()
#exit()-stop and exit programme

	input_bars_weight(int(bars_amount),1)
	print("Your max amount of gold: ",count_weight(int(capacity), int(bars_amount)))
	return 0

def input_bars_weight(bars_amount,amount_index):
#main_input()-get value of each bar

	error_index=1
	while error_index:
		try:
			error_index=0
			print(amount_index,end='')
			bag_weight.append(int(input(" bar's weight: ")))
#append()-add items to list

		except ValueError:
			error_index=1
			print("You can't write in this way!Try again!")
	return input_bars_weight(bars_amount,amount_index+1) if amount_index < bars_amount else None

def count_weight(capacity, bars_amount):
#count_weight()-searching the best combination of bars

	if bars_amount == 0 or capacity == 0:
		return 0
	if bag_weight[bars_amount - 1] > capacity:
		return count_weight(capacity, bars_amount - 1)
	else:
		return max(bag_weight[bars_amount-1] + count_weight(capacity-bag_weight[bars_amount-1],bars_amount-1),
		count_weight(capacity, bars_amount-1))
#max()-choosing the biggest value

bag_weight=[]
main_input()