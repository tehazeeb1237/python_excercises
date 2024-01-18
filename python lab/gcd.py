def gcd(a, b):                #a=24 b=36
    while b != 0:
        a, b = b, b % a            #a=36,b=12     a=12 b=0
    return a        #a=12

# Example usage
num1 = int(input("Enter the num1 value:"))
num2 = int(input("Enter the num2 value:"))

result = gcd(num1, num2)         #result=12
print("GCD of", num1, "and", num2, "is:", result)

