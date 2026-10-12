#1 The first bug I spotted was from the traceback because the treaceback helped helped guide me back to where the error occured. I learned that I am starting to use error messages to identify problems. I still need practice but I am getting better at understanding errors and finding the root of the problem. 
#2 This code takes a price and a discount tier as inputs. Python uses the tier to detirmine how much of a discount should be given, A colleague could use this function without reading the body, it will work as long as the function name, inputs, and values are clear. 
#3 AI disclosure: I used chatGPT to help explain debugging concepts and aid me in percicely finding the issue within my code causing it to not run. Reflection: Using AI helped me deepen my understanding because I was able to identify my mistakes and correct them, it did not simply give me the answer but instead helped me to get started and learn how to find an error and correct it. 

#exercise 1 

def calculate_tax(price, rate):
    return price * rate

#calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold" :
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price  # No discount for unrecognized tiers

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') =  ${final_price(200, 0.07, 'gold'):.2f}")

#Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (50, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

#Exercise 5



#Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)


