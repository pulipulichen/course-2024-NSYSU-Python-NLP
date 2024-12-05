# 讀取input.txt

# Initialize the input_string variable.
input_string = "" 

# Load input.txt content to input_string.
with open('input.txt', 'r') as file:
  input_string = file.read()
  
# Display the input_string int the result.
input_string