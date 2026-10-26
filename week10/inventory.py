# Reflection Question 1:
# The most surprising thing about Python lists is how easy they are to
# modify. I did not expect to be able to add, remove, sort, and access
# items with such simple commands and indexing.

# Reflection Question 2:
# A Python list would have been useful for tracking sales data in a class
# project. Instead of manually entering formulas in Excel, Python could
# quickly calculate totals, averages, and identify the best and worst sales days.


# ==========================
# EXERCISE 1 - Build the list
# ==========================

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# ==========================
# EXERCISE 2 - Index practice
# ==========================

print(inventory[0])  # first item
print(inventory[-1])  # last item

middle_index = len(inventory) // 2
print(inventory[middle_index])


# ==========================
# EXERCISE 3 - Slicing
# ==========================

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# ==========================
# EXERCISE 4 - Modify
# ==========================

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# ==========================
# EXERCISE 5 - Tuple comparison
# ==========================

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples cannot be changed. This makes tuples useful for storing fixed coordinates.")

print(coords)


# ==========================
# EXERCISE 6 - Average of sales
# ==========================

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# ==========================
# EXERCISE 7 - Accumulator pattern
# ==========================

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)


# ==========================
# EXERCISE 8 - Filter above threshold
# ==========================

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High Sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))