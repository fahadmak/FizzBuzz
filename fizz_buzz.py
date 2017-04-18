
def fizz_buzz(num):
    '''
    if number divisible by 3 return 'fizz';
    5, 'buzz'; both, fizzbuzz
    else return number
    '''
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num
print (fizz_buzz(45))

