Define the problem statement?
-the main problem is calculate the total of the user order
What are the Inputs?
-Customer name, Coffee quantity, Tea quantity, Sandwich quantity
What are the output?
-the receiot including Customer name, Coffe, Tea and Sandwich quantity and finally the total
What would be the typical process flow?
-first writing the Calculate total function including the input multiply by the price and finally return the total, secound the printing functhion
What is the constraints?
-the prices are fixed and can't be change, the programme allow only even quantity, Name of the costomer must be full not empty, the programme calculate only one receipt at a time
How to decompose the programme?
-first define the prices and the input then move intp the calculating process and finally the printing process
Write the pseudocode:
coffee_price = 8.50
Tea_price = 6.00
Sandwich_price = 12.00
name = input("Customer name")
Coffee = int(input("coffee quantity"))
Tea = int(input("Tea quantity"))
Sandwich = int(input("Sandwich quantity"))

def calculate_total(coffee, tea, sandwich):
total = (coffee*coffee_price)+(tea*tea_price)+(sandwich*sandwich_price)
return total

def print_receipt(name, coffee, tea, sandwich, total):
print("RECEIPT")
print(f"Customer :{name}")
print(f"Coffee :{coffee}")
print(f"Tea :{tea}")
print(f"Sandwich :{sandwich}")
print("-----------------")
