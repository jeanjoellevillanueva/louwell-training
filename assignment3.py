
# Assignment 1:
# Create a function that will print countries that start with P or p.

# Assignment 2:
# Create a function that will ask for user input (numbers 1-27 pertaining to a-z)
# Every loop, Tatanungin if input is finished or no.
# Input: 1 -> Output: a
# Input: 1,16,16,12,5 -> Output: apple

# Clue: while loop, list, dict, ifelse

places_that_starts_with_p_and_m = [
    "manila", "Paris", "Madrid", "Melbourne", "Moscow",
    "Palermo", "perth", "Mumbai", "Munich", "portland",
    "Prague", "Marseille", "pune", "Miami", "Phnom Penh"
]

def places_that_start_with_letter_p_and_P(places):
    for place in places:
        if place.startswith('p') or place.startswith('P'):
            print(place)
        

def ask_for_user_input():
    user_answer = 'no'
    converter_dict = {
        '1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        '10': 'j',
        '11': 'k',
        '12': 'l',
        '13': 'm',
        '14': 'n',
        '15': 'o',
        '16': 'p',
        '17': 'q',
        '18': 'r',
        '19': 's',
        '20': 't',
        '21': 'u',
        '22': 'v',
        '23': 'w',
        '24': 'x',
        '25': 'y',
        '26': 'z'
    }
    word = ''
    while user_answer == 'no':
        user_input = input('Please enter a number from 1 - 26: ') # 1 - 26 need mo mag print: Please enter a number between 1-26
        user_answer = input('Tapos kana ba? yes/no: ') # Please choose only between yes or no. Yes/YES/yES - accepted
        letter = converter_dict[user_input]
        word += letter # word = word + letter
    print(word)

if __name__ == '__main__':
    #places_that_start_with_letter_p_and_P(places_that_starts_with_p_and_m)
    ask_for_user_input()









