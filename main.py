def is_Palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


print(is_Palindrome("Hi"))
