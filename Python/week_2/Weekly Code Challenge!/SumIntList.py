int_list = []
while True :
    user_input = input("Enter a number or type 'exit' to stop : ")
    
    if user_input.lower() == "exit":
        print("\n Exiting program...")
        break


    try:
        number= int(user_input)
        int_list.append(number)
    except ValueError:
        print("enter valid number")
print(f"\n total sum is : {sum(int_list)}")
