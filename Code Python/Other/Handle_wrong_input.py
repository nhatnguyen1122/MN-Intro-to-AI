# while True:
#     num = input("Enter a number: ")
#     try:
#         num = int(num)
#         break
#     except ValueError:
#         print("You didn't enter a number.")

# print("Your number is " + str(num))

while True:
    num = input("Enter a number: ")
    if (num.isdigit()):
        break
    else:
        print("You didn't enter a number.")

print("Your entered {0}".format(num))