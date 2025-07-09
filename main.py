x = 'b'
y = 'cd'
print(x + y)


fruit_list = ['apple', 'pineapple','banana']
# add: append
# remove: pop

# fruit_list.append('mango')
# fruit_list.pop()
# fruit_list.pop()

person_dict = {'name': 'Louwell', 'age': 23}

print(person_dict.get('gender', 'male'))

# Function
def sum(x, y):
    print(x + y)

def multiply(z, r):
    print(z * r)

sum_numbers = sum(1, 5)
sum2_numbers = sum(3, 4)

diff_numbers = multiply(3, 1)

print(sum_numbers)
print(sum2_numbers)

print(diff_numbers)

"""
Assignment:

1. Define a function: Sum three numbers and minus 4th.
eg. func(1,2,2,4) -> Ans: 1

2. Function that will print age:
eg. asd = {'name': 'Joelle','age': 29,} -> Ans: 29

3. Function remove 2 items sa list:
eg. lists = ['1', '2', 'apple', 'banana'] -> Ans: ['1', '2']
"""