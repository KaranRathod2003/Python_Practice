#7. Coffee Customization
#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_size = "Medium"
extra_shot = False
if extra_shot:
    coffee = order_size + " Coffee With Extra shot"
else:
    coffee = order_size + " Coffee"
print("Order for,",coffee)