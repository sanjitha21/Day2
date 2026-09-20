records= ('p101,pA,1000',
          'p102,pB,2000',
          'p103,pC,3000',
          'p104,pD,4000',)
#iterate a records
#display product name in uppercase
#calculate sum of product cost
#display tottal product cost at the end
total_cost = 0
for record in records:
    product_details = record.split(',')
    product_name = product_details[1].upper()
    product_cost = int(product_details[2])
    total_cost += product_cost
    print(f"Product Name: {product_name}, Product Cost: {product_cost}")

print(f"Total Product Cost: {total_cost}")

#enumerate() function in python
#The enumerate() function in Python adds a counter to an iterable and returns it as an enumerate
for i, record in enumerate(records):
    product_details = record.split(',')
    product_name = product_details[1].upper()
    product_cost = int(product_details[2])
    print(f"Index: {i}, Product Name: {product_name}, Product Cost: {product_cost}")
    