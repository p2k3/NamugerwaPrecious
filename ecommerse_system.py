
# E-COMMERCE SYSTEM WITH LOGIN


# User lists
admins = ["admin"]
customers = ["john", "mary"]
cashiers = ["cash1"]

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    print("\nWELCOME,LOGIN TO YOUR ACCOUNT")

    username = input("Enter username: ")
    password = input("Enter password: ")

    
    # ADMIN LOGIN
    
    if username in admins:

        if password == "admin123":

            print("\nLogin Successful!")
            print("Role: Admin")
            print("Access Level: Full System Access")

            break

        else:
            print("Incorrect Admin Password")
            attempts += 1

    
    # CUSTOMER LOGIN
    
    elif username in customers:

        if password == "customer123":

            print("\nLogin Successful!")
            print("Role: Customer")
            print("Access Level: Shopping System")

            
            # SHOPPING SECTION
            

            subtotal = float(input("\nEnter subtotal amount: "))

            coupon = input("Enter coupon code: ")

            location = input("Enter location: ")

            # Discount calculation
            if coupon == "SAVE10":
                discount = subtotal * 0.10

            elif coupon == "SAVE20":
                discount = subtotal * 0.20

            else:
                discount = 0
                print("Invalid coupon code.")

            # Tax based on location
            if location == "Kampala":
                tax_rate = 0.18

            elif location == "Entebbe":
                tax_rate = 0.15

            else:
                tax_rate = 0.10

            # Nested condition for extra tax
            if subtotal > 500000:
                tax_rate += 0.02

            elif subtotal > 200000:
                tax_rate += 0.01

            # Final calculations
            price_after_discount = subtotal - discount
            tax = price_after_discount * tax_rate
            final_price = price_after_discount + tax

            # Receipt
            print("\n===== RECEIPT =====")
            print(f"Subtotal: UGX {subtotal:,.0f}")
            print(f"Discount: UGX {discount:,.0f}")
            print(f"Tax: UGX {tax:,.0f}")
            print(f"Final Price: UGX {final_price:,.0f}")

            break

        else:
            print("Incorrect Customer Password")
            attempts += 1

    
    # CASHIER LOGIN
    
    elif username in cashiers:

        if password == "cashier123":

            print("\nLogin Successful!")
            print("Role: Cashier")
            print("Access Level: Payment Processing")

            amount = float(input("Enter payment amount: "))

            print(f"Payment of UGX {amount:,.0f} processed successfully.")

            break

        else:
            print("Incorrect Cashier Password")
            attempts += 1

    
    # USER NOT FOUND
    else:
        print("User not found.")
        attempts += 1


# ACCOUNT LOCK

if attempts == max_attempts:
    print("\nMaximum login attempts reached.")
    print("Access denied.")