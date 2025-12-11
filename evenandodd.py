import sys

# Default values if user does not provide input
default_numbers = [5, 10, 15]

# If user provides numbers, use them; otherwise use defaults
if len(sys.argv) > 1:
    numbers = list(map(int, sys.argv[1:]))
    source = "User Input"
else:
    numbers = default_numbers
    source = "Self-assigned"

print(f"{source} Numbers: {numbers}")

# Count evens and odds
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)

print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
