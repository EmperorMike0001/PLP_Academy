PersonInfo = {}

while True:

    print("\n Current Information")
    for keys , values in PersonInfo.items():
        print(f"\n {keys} : {values}")

    user_input = input("Enter 'name' to update your name, 'age' to update your age , 'color' to update your favourite color  , 'new'  to  enter afresh or type 'exit' to stop ")

    if user_input.lower() == "exit":
        print("Exiting program...")
        break

    elif user_input.lower() == "name":
        user_name=input("enter your name : ")
        PersonInfo["name"] = user_name.capitalize()
    
    elif user_input.lower() == "age":
        user_age=input("enter your age : ")
        try: 
            Age =int(user_age)
            PersonInfo["age"] = Age
        except ValueError:
            print(" Invalid age! Enter a number :")

    elif user_input.lower() == "color":
        user_color=input("enter your fovaurite color :")
        PersonInfo["favourite color"] = user_color.capitalize()
    else:
        print("Invalid input !!! type 'name' , 'age' , 'color', 'exit'  ")

   

print(f"\n Updated Information")
for person in PersonInfo:

    print(f"\n {person} : {PersonInfo[person]} ")