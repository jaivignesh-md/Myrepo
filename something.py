def is_palindrome(input_str):
    # Convert the input string to lowercase and remove any whitespace
    input_str = input_str.lower().replace(" ", "")
    
    # Reverse the input string
    reversed_str = input_str[::-1]
    
    # Check if the input string is equal to its reverse
    if input_str == reversed_str:
        return True
    else:
        return False

# Example usage
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")