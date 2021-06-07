def get_month_decorator(func):
    """ checks that number being passed as month argument is valid. i.e betweeen 1 - 12"""


# calling the decorator unto the function
@get_month_decorator
def get_month(month):
    """ returns the expected month string based on the valid month integer passed as an argument """
