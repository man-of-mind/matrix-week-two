import argparse

parser = argparse.ArgumentParser()
#a variable to store a strnig argument
str_arg = parser.add_argument('str')

def get_month_decorator(func):
    def inner(n):
        if n not in range(1, 13):
            raise argparse.ArgumentError(str_arg, 'The number has to be between 1 and 12')
        return func(n)
    return inner


@get_month_decorator
def get_month(n):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', \
        9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return months.get(n)


user_input = input("Enter number: ")
try:
    print(get_month(int(user_input)))
except ValueError:
    print('The number must be a valid integer')

