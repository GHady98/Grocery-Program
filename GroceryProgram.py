groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

cart = {}  
while True:
    item = input("What do you want to buy? ")
    
    if item.lower() == "done":
        break

   
    parts = item.split()
    if len(parts) == 2 and parts[1].isdigit():
        item_name = parts[0].lower()
        quantity = int(parts[1])
    else:
        item_name = item.lower()
        quantity = 1
    
    if item_name in groceries:
        cart[item_name] = cart.get(item_name, 0) + quantity
    else:
        print("Sorry, we don’t have that item.")


total = 0
for item, qty in cart.items():
    price = groceries[item]

    
    if item == "milk" and qty > 2:
        price -= 1

    total += price * qty

print("\nYou bought:", cart)
print("Total = $", total)

if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")