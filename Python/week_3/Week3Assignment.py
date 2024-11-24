'''1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
   The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
   If the discount is 20% or higher, apply the discount; otherwise, return the original price.'''

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    if discount_percent >= 20:
        final_price = price - discount
        return final_price
    else :
        return price

#final_price = calculate_discount(price ,discount_percent)
#print(f"\nTotal : {final_price}")

'''2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
  Print the final price after applying the discount, or if no discount was applied, print the original price.'''

while True:
        
    user_choice= input("type 'price' to enter price, type 'discount' to enter discount percentage : ").strip().lower()
    if user_choice == "q":
        break

    
    

    if user_choice == "price":
        item_price = input("enter item price : ")
        price =int(item_price)

    elif user_choice == "discount":
        item_discount = input("enter item discount : ")
        discount_percent = int(item_discount)
    else :
        print("invalid input !! ")
        exit()
    

    
final_price = calculate_discount(price, discount_percent)
print(f"\nTotal : {final_price}")