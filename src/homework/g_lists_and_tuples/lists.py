def test_config():
    return True

def get_lowest_list_values(list1):
    lowest = list1[0]
    indx = 0
    length = 0
    for num in list1:
        length += num
    while indx < length:
    #while indx < len(list1):
        for num in list1:
            if num < lowest:
                lowest = num
            indx += 1
    return lowest

def get_highest_list_values(list1):
    highest = list1[0]
    indx = 0
    length = 0
    for num in list1:
        length += num
    while indx < length:
    #while indx < len(list1):
        for num in list1:
            if num > highest:
                highest = num
            indx += 1
    return highest