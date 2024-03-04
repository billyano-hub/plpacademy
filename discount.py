def calculate_discount(price,discount_percent):
    if discount_percent >= 20 :
        final_price=int(price * (1-discount_percent/100))
        return final_price
    else:
        return price

price=int(input("Enter the price"))
discount_percent=int(input("Enter discount_percent"))
final_price = calculate_discount(price, discount_percent)
print(f"The price is #{final_price:.2f}")