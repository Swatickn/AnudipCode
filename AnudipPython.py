# Function to find the GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the GCD
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
