num = list()
num.append(8)
print(num)


numbers = [17,8,2024,3,1998,2005,]
nums = (input("\n Enter Number "))

try:
    nums = int(nums)
    if nums not in numbers:
        print(f"wrong ")
    else:
        print(f"correct {nums}")
except ValueError:
    print("invalid input !!!")


stack = [17,8,2024,3,1998,2005,]
print(stack.pop())
print(f"updated stack {stack}")
stack.append(16)
print(f"updated 2 stack {stack}")


