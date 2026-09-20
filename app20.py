#explain pop() method in python with example
# The pop() method in Python is used to remove and return an element from a list. By default, it removes the last item in the list, but you can also specify an index to remove a specific item. If the list is empty and you try to pop an element, it will raise an IndexError.
# Example:
my_list = [1, 2, 3]
popped_element = my_list.pop()
print(f"Popped element: {popped_element}")  # Output: Popped element: 3
print(f"Remaining list: {my_list}")  # Output: Remaining list: [1, 2]
