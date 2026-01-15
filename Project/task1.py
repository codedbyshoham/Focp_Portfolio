import math

def get_price(i):
    while True:
        try:
            val = float(input(f"Enter Price of Pizza #{i}: "))
            if val > 0: return val
        except ValueError:
            pass # Just ignore errors and ask again
        print("Invalid price.")

print("Beckett Pizza Plaza 4-for-3 Offer\n=================================\n")

prices = []
for i in range(1, 5):
    prices.append(get_price(i))

savings = min(prices)
total = sum(prices) - savings
percent = math.ceil((savings / sum(prices)) * 100)

print(f"\nOrder Total is \u00A3{total:.2f}, a fabulous discount of {percent}%!")
