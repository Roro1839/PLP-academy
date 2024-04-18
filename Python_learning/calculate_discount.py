#!/usr/bin/python3

def calculate_discount(price, discount_percent):
    answer = price - (discount_percent/100 * price)
    if discount_percent >= 20:
        return answer
    else:
        return price

price = input("Enter the original price: ")
discount_percent = input("Enter the discount percentage: ")

print(calculate_discount(float(price), float(discount_percent)))
