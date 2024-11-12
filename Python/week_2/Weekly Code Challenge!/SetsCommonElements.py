print(f"\n Common Elements in 2 Sets")

Set_1 = set()
Set_1 = {2,2,3,7,88,8}
Set_2 = set()
Set_2 = {2,3,7,88,8}
while True:
    input_data = input("\ntype '1' to update set 1 , type '2' to update set 2 or type 'q' to exit : ")

    if input_data == "q":
        print("\nExiting program...")
        break

    elif input_data == "1":
        input_1 = input("enter a number to set 1 : ")
        try:
            input1 = int(input_1)
            Set_1.add(input1)
            print(f"Updated Set 1: {Set_1}")
        except ValueError:
            print("invalid input !! please a number")
    elif input_data == "2" :
        input_2 = input("enter set 2 number : ")
        try:
            input2 = int(input_2)
            Set_2.add(input2)
            print(f"Updated Set 2: {Set_2}")
        except ValueError:
            print("invalid input !! please a number")
    else:
        print("invalid input !! please type '1' , '2' or 'q' ")


common_elements = Set_1.intersection(Set_2)
print(Set_1)
print(Set_2)

print(f"\nCommon Elements are : {common_elements}")
