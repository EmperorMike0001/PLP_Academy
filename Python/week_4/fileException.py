
try:
    with open("noneexistent.txt","r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("file not found. please check the file name")


try:
    with open("sample.txt", "r") as file:
        data= file.read()
except FileNotFoundError:
    print("file not found")
finally:
    try:
        file.close()  # This will close the file if it was successfully opened
    except NameError:
        # If 'file' was never opened, this will catch the exception
        print("No file was opened.")