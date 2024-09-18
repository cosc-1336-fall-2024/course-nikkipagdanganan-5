import decisions

def main():
    option = int(input('Enter option: '))
    total = int(input('Enter total: '))
    result = option/total

    ratio = decisions.get_options_ratio(option, total)

    rating = decisions.get_faculty_rating(ratio)

    print ('The faculty rating is: ', rating)

main()

