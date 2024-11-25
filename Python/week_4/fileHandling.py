import os
# creating empty file
file2 = open("input.txt")


#opening a file
file= open("output.txt")

#writing on a file

with open ("output.txt" , "w") as file: file.write("i love python \n")
#with open ("input.txt" , "w") as file2: file2.write("i love python programming\n")
#appending on a file

with open ("output.txt" , "a") as file:
     file.write("hello python \n")
     file.write("Code with Mike\n")
#reading in a file

with open ("output.txt" , "r") as file: data = file.read()  
print("Output file content:\n", data)
with open ("input.txt" , "r") as file: data2 = file.read()  
print("input file content:\n",data2)

# merging a file with a another file
# Merging content from input.txt into output.txt

with open("output.txt", "a") as file:
    with open("input.txt", "r") as file2:
        for line in file2:
            file.write(line)

# Verify that the content from both files is merged in output.txt
with open("output.txt", "r") as file:
    merged_data = file.read()
print("Merged file content:\n", merged_data)

# reading an image
''' image = open("logo.jpg", "rb")
for i in image:
    print(i)

# Copying the image into another file

copyImg = open("logo.jpg", "wb")
for i in image:
    copyImg.write(i)

'''

# removing a file
# import the os module
os.remove(filename)

