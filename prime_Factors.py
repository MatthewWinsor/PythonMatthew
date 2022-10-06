
PRIME_NUMBERS = []
def number_prime_or_not(number):
    if number > 1:
        for numbers in range(2, number):
            if (number % numbers) == 0:
                PRIME_NUMBERS.append(numbers)
            else:
                pass
    else:
        return "No prime or negitive number"
    return PRIME_NUMBERS
