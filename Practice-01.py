# Conditional statements sample program with PEP 8 Formatting
def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Please enter a number=\t"))
result = odd_or_even(number)
print(result)
