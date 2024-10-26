def test_config():
    return True

def get_p_distance(list1, list2):
    # need to compare each value is the list to each other 
    # find total number of difference between the lists compared and that's p_distance 
    # so look for how to do it on one comparison and then loop function to do to all the rest
    indx = 0
    count = 0
    dp = []
    for i in list1:
        if list1[indx] != list2[indx]:
            count += 1
        indx += 1
  
    dp = count / len(list1)
    return dp

def get_p_distance_matrix(list1):
    dpmatrix = []
    for i in range(len(list1)):
        row = []
        for j in range(len(list1)):
            dpnum = get_p_distance(list1[i], list1[j])
            row.append(dpnum)
        dpmatrix.append(row)
    return dpmatrix