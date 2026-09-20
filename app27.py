#explain len() function in python with example
# The len() function in Python is used to determine the number of items in an object. It can be used with various data types such as strings, lists, tuples, dictionaries, and more. The function returns an integer representing the length of the object.
# Example 1: Using len() with a string
my_string = "Hello, World!"
print(f"Length of the string: {len(my_string)}")  # Output: Length of the string: 13

# Example 2: Using len() with a list
my_list = [1, 2, 3, 4, 5]
print(f"Length of the list: {len(my_list)}")  # Output: Length of the list: 5

# Example 3: Using len() with a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"Length of the tuple: {len(my_tuple)}")  # Output: Length of the tuple: 5

# Example 4: Using len() with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print(f"Length of the dictionary: {len(my_dict)}")  # Output: Length of the dictionary: 3
#use while conditional statement
i = 0
while i < len(my_list):
    print(f"Element at index {i}: {my_list[i]}")
    i += 1  
#use for loop conditional statement
for index in range(len(my_list)):
    print(f"Element at index {index}: {my_list[index]}")        
    