def check_palindrome(value):
    if len(value) <= 1:
        return True
    if value[0] != value[-1]:
        return False
    return check_palindrome(value[1:-1])

    
given_string = input("Enter something: ")
if check_palindrome(given_string):
    print("{} is a palindrome".format(given_string))
else:
    print("{} is not a palindrome".format(given_string))