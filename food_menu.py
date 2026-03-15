print("------ Welcome to Jorsi Food Shop ------")

print("Menu")
print("1. Pizza - ₹120")
print("2. Burger - ₹80")
print("3. Sandwich - ₹60")
print("4. Juice - ₹40")

choice = int(input("Enter your choice (1-4): "))
qty = int(input("Enter quantity: "))

if choice == 1:
    price = 120
    item = "Pizza"
elif choice == 2:
    price = 80
    item = "Burger"
elif choice == 3:
    price = 60
    item = "Sandwich"
elif choice == 4:
    price = 40
    item = "Juice"
else:
    print("Invalid choice")
    exit()

total = price * qty

print("\n----- BILL -----")
print("Item:", item)
print("Quantity:", qty)
print("Total Price: ₹", total)
print("Thank you for visiting!")