from functools import reduce

def is_palindrome_reduce(input_string):
    return reduce(lambda x, y: x and y, [input_string[i] == input_string[-(i+1)] for i in range(len(input_string)//2)])

# Example usage
input_string = "madam"
print(is_palindrome_reduce(input_string))  # Output: True
