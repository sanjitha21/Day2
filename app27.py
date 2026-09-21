
my_string = "Hello, World!"
print(f"Length of the string: {len(my_string)}")  

my_list = [1, 2, 3, 4, 5]
print(f"Length of the list: {len(my_list)}")  


my_tuple = (1, 2, 3, 4, 5)
print(f"Length of the tuple: {len(my_tuple)}") 


my_dict = {"a": 1, "b": 2, "c": 3}
print(f"Length of the dictionary: {len(my_dict)}") 

i = 0
while i < len(my_list):
    print(f"Element at index {i}: {my_list[i]}")
    i += 1  

for index in range(len(my_list)):
    print(f"Element at index {index}: {my_list[index]}")        
    
