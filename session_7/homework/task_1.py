# Create a function calculate_final_price(price, tax_rate=0.07, discount=0.10) that:
#  - Returns the final price after both operations (tax first, then discount)

# Output:
# calculate_final_price(100) == 96.3
# calculate_final_price(200, 0.08) == 192.6



def calculate_final_price(price, tax=1.57, discount=5):
    tax_price = price - tax
    discount_price = tax_price - discount
    return discount_price

print(calculate_final_price(100))
