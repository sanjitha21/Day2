#explain dictionary with example
# A dictionary in Python is a collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable, meaning you can change their content without changing their identity.
# Example:
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)
print(f"Type of student: {type(student)}")  # Output: Type of student: <class 'dict'>
#how to get/fetch nth item from given dict
#dictname['key'] -> value/keyerror
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A
#how to modify an existing dict -value
student["age"] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21,

#how to add new data to an existing dict
student["city"] = "New York"
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A', 'city': 'New York'}