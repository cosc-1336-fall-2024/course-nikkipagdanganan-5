import strings

def main():
    print ("""
    1-Hammering Distance
    2-Dna Complement
    3-Exit
    """)

    prompt = int(input('Select a number to choose an action.'))

    if prompt == 1:
        x1 = input('Enter the first of two DNA strings to get hamming distance: ')
        x2 = input('Enter the second of two DNA strings to get hamming distance: ')
        answer = strings.get_hamming_distance(x1, x2)
        print(f'The Hammering Distance is: {answer}.')

    elif prompt == 2:
        dnarev = input('Enter a DNA string to get the complement: ')
        answer2 = strings.get_dna_complement(dnarev)
        print(f'The DNA complement is: {answer2}.')

    else:
        print('Goodbye.')
main()
