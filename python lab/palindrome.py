def palindrome(string):
    string=string.lower()
    reversed_string=string[::-1]
    if string==reversed_string:
        return True
    else:
        return False
    
result=palindrome("mom")
print(result)
