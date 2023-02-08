def bakery_sale(loaves):
    regular_price=185*loaves
    discount=0.6*regular_price
    total_price=regular_price-discount
    return regular_price,discount,total_price
loaves=int(input("enter the number of loaves of day old bread:"))
regular_price,discount,total_price=bakery_sale(loaves)

print("Regualar_prices: {:.2f} rupees".format(regular_price))
print("Discount:{:.2f} rupees".format(discount))
print("total price:{:.2f} rupees".format(total_price))
