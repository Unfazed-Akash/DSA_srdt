# Q6: Minimum Discount Item
# Clothing: 20% off, Shoe: 10% off, Laptop: 5% off
# Accept price for each item, find item with minimum absolute discount amount

clothing_price = float(input("Enter price of clothing: "))
shoe_price = float(input("Enter price of shoe: "))
laptop_price = float(input("Enter price of laptop: "))

clothing_discount = clothing_price * 20 / 100
shoe_discount = shoe_price * 10 / 100
laptop_discount = laptop_price * 5 / 100

print(f"\nClothing discount : {clothing_discount:.2f}")
print(f"Shoe discount     : {shoe_discount:.2f}")
print(f"Laptop discount   : {laptop_discount:.2f}")

discounts = {
    "Clothing": clothing_discount,
    "Shoe": shoe_discount,
    "Laptop": laptop_discount,
}

min_item = min(discounts, key=discounts.get)
print(f"\nItem with minimum discount offer: {min_item} (Discount amount: {discounts[min_item]:.2f})")
