#Create a program that reads a file and writes a modified version to a new file
file = open("file.txt",)


with open("file.txt","r") as file:
    data=file.read()
#print("The file content is: \n ", data)

modifieddata= data.upper()

with open("modified.txt", "w") as file2:
    file2.write(modifieddata)

'''with open("modified.txt", "r") as file2:
    print("modified content:\n", file2.read()) '''


#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    user_input = input("Enter the file name : ")
    with open(user_input,"r") as file:
        data=file.read()
        print(data)


except FileNotFoundError:
    print(f"file {user_input} not found !!! please check the file name ")

except IOError:
    print("An error occurred while reading the file.") 