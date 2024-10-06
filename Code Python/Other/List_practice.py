def convert_and_check(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        pass

    try: 
        float_value = float(value)
        return float_value
    except ValueError:
        pass

    try:
        complex_value = complex(value)
        return complex_value
    except ValueError:
        pass

    return value

while True:
    number_of_list = input("Enter the number of lists: ")
    if (number_of_list.isdigit()):
        break
    else:
        print("Please enter only integers.")

number_of_list = int(number_of_list)
final_list = []
for i in range(number_of_list):
    amount_of_elements_in_each_list = int(input("Enter the number of elements in list {}: ".format(i+1)))
    for j in range(amount_of_elements_in_each_list):
        each_element = input("Enter element {} in the list {}: ".format(j+1, i+1))
        final_list.append(each_element)

int_list = []
float_list = []
complex_list = []
string_list = []

for i in final_list:
    i = convert_and_check(i)
    if (isinstance(i, int)):
        int_list.append(i)
    elif (isinstance(i, float)):
        float_list.append(i)
    elif (isinstance(i, complex)):
        complex_list.append(i)
    else:
        string_list.append(i)

print("Integers are: ")
for x in int_list:
    print(x)
print("Floats are: ")
for x in float_list:
    print(x)
print("Complex are: ")
for x in complex_list:
    print(x)
print("Strings are: ")
for x in string_list:
    print(x)