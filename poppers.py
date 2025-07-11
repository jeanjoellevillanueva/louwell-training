lists_places = ['Baguio', 'Bulacan', 'Pampanga', 'Manila']
lists_places.pop(3)
print (lists_places)

lists_places.pop(2)
print (lists_places)

lists_places2 = ['Baguio', 'Bulacan', 'Pampanga', 'Manila']


def remove_last(list_of_place):
    """
    Remove the last on the list.
    """
    sliced_list = list_of_place[:-2]
    print('From function: ', sliced_list)
    return sliced_list


remove_last(lists_places2)
