#!/usr/bin/env python3
# -*- coding: ascii -*-
import os, sys

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage (e.g., 20 for 20%).
    Returns:
        float: The final price after applying the discount.
    """

    if discount_percent >= 20:
        # Apply the discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
    else:
        # No discount applied
        final_price = price
    return final_price

# Get input from the user
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"Final price after applying the discount: ${final_price:.2f}")
