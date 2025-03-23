food = []
prices = []
total = 0
while True:
    item = input("Enter food ---buy :(q -->quit): ")
    if item == "q":
        break
    else: 
        price = float(input(f"Enter price of {item}:$"))
        food.append(item)
        prices.append(price)
print("-----YOUR CART-----")
for item in food:  # Fixed loop to iterate over the 'food' list
    print(f"- {item}")  # Improved formatting for better readability
for price in prices:
    total += price    
print(f"\nTotal: ${total}")
