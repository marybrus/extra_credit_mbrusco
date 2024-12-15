import re

def is_in_union(input_string):
    # Define the patterns for A and B
    pattern_a = re.compile(r"^a*$")  # Zero or more 'a's
    pattern_b = re.compile(r"^B+$")  # One or more 'B's

    # Check if the input matches either pattern
    if pattern_a.match(input_string) or pattern_b.match(input_string):
        return True
    return False

# Get input from the user
user_input = input("Enter a string: ")

# Check if the input is in the union of A and B
if is_in_union(user_input):
    print("The input is in the union of A and B.")
else:
    print("The input is NOT in the union of A and B.")
