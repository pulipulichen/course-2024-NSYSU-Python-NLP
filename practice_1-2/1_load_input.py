"""
讀取input.txt
"""

# Initialize the input_string variable.
input_string = "" 

# Load the content of input.txt to input_string.
with open('input.txt', 'r') as file:
  input_string = file.read()
  
# Display the input_string int the result.
input_string