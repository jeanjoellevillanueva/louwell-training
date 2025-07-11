# for variable in variables:
# List
places = ['Manila', 'Baguio', 'Malolos']

if __name__ == '__main__':
    print(places[0])
    print(places[1])
    print(places[2])

    for place in places:
        print('From for loop: ', place)


    # Dict
    employee_info = {
        'name': 'Louwell',
        'age': 23,
        'salary': 10000
    }
    print(employee_info['name'])
    print(employee_info['age'])
    print(employee_info['salary'])
    for _, value in employee_info.items():
        print('From for loop: ', value)

    # Range
    for number in range(4, 12, 3):
        print(number)