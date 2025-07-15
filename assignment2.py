"""
1. Create a func print: ping if number is divisible by even. else: pong
- input
- use function for reusability.

2. create a function that will print places starting with letter 'M'
places = [
    "Manila", "Paris", "Madrid", "Melbourne", "Moscow",
    "Palermo", "Perth", "Mumbai", "Munich", "Portland",
    "Prague", "Marseille", "Pune", "Miami", "Phnom Penh"
]

3. create a function that will compute the backpay of a resigned employee.
backpay = number_years * salary per month
- use input for salary and number of stay
- store it on dict
- compute backpay
"""

""" 1 """
def divisible(number, divisor):
    """ Check if the number is divisible by even number """

    if number % divisor == 0:
        print ("ping")
    else:
        print ("pong")


""" 2 """

places_that_starts_with_p_and_m = [
    "Manila", "Paris", "Madrid", "Melbourne", "Moscow",
    "Palermo", "Perth", "Mumbai", "Munich", "Portland",
    "Prague", "Marseille", "Pune", "Miami", "Phnom Penh"
    ]

def places_that_start_with_letter_m(places):
    for place in places:
        if place.startswith('M'):
            print(place)


# """ 3 """

# #dict

def backpay(number_of_stay, salary):

    employee_details= {
        'number_of_stay': number_of_stay ,
        'salary': salary 
    }

    print(employee_details['number_of_stay'] * employee_details['salary'])


if __name__ == '__main__':
    number = int(input('Put number here:'))
    divisor = int(input ('Put divisor here:'))
    divisible(number, divisor)
    places_that_start_with_letter_m(places_that_starts_with_p_and_m)    
    number_of_stay = int(input('Put number_of_stay here'))
    salary = int(input('Put salary here'))
    backpay(number_of_stay,salary)



