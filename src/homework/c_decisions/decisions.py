def test_config():
    return True

def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    rating = ""

    if ratio >= .9 and ratio <1:
        rating = 'Excellent'
    elif ratio > .8:
        rating = 'Very Good'
    elif ratio > .7:
        rating = 'Good'
    elif ratio > .6:
        rating = 'Needs Improvement'
    elif ratio > 0 and ratio < .59:
        rating = 'Unacceptable'

    return rating

