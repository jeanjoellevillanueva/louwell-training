people = {
    'name': 'John', 'ages': '35' 
}

def get_age(person_dict):
    """
    Returns the age of the person.
    """
    age = person_dict['age']
    print('From function: ', age)
    return age

get_age(people)
