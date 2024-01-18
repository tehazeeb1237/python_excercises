num = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Counter variable
count = 0

# Check if the number of terms is valid
if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print("Fibonacci sequence up to", num, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < num:
        print(a)
        nth = a + b
        # Update values for the next iteration
        a = b
        b = nth
        count += 1


