def bars_weight(bars_amount):
    for i in range(bars_amount):
        weight.append(int(input("Bar's weight: ")))
    pass
def bag(capacity, weight, bars_amount):
    if bars_amount == 0 or capacity == 0:
        return 0
    return bag(capacity, weight, bars_amount - 1) if weight[bars_amount - 1] > capacity else max(weight[bars_amount - 1] + bag(capacity - weight[bars_amount - 1], weight,bars_amount - 1),bag(capacity, weight, bars_amount - 1))
capacity = int(input("Capacity of bag: "))
bars_amount = int(input("Number of different bars: "))
weight = []
bars_weight(bars_amount)
print("Your max amount of gold: ",bag(capacity, weight, bars_amount))