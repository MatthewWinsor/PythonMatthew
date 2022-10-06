
PRIME_NUMBERS = []
def number_prime_or_not(number):
    try:
        int(number)
        PRIME_NUMBERS.append(number)
    except ValueError:
        print("That's not a number sorry")


    if number > 1:
        for numbers in range(2, number):
            if (number % numbers) == 0:
                PRIME_NUMBERS.append(numbers)
            else:
                pass
    else:
        return PRIME_NUMBERS
    return PRIME_NUMBERS
