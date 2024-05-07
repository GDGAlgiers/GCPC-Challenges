def sol(items, price):
    items = sorted([int(item[1:]) for item in items])
    price = int(price[1:])
    items_count = 0

    for item in items:
        if item <= price:
            items_count += 1
            price -= item
        else:
            break

    if items_count == 0:
        return "Insufficient cash!"
    else:
        return items_count

items_list = []
total_price = ""

items_input = input("").split()
total_price = input("")

print(sol(items_input, total_price))
