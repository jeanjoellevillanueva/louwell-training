
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


if __name__ == '__main__':
    places_that_start_with_letter_p_and_P(places_that_starts_with_p_and_m)









