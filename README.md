## ASSESSMENTS

Below are tasks that you are expected to complete and provide solutions to in the python scripts in the src folder. Enjoy!

## Task 1

(a) Using the iteration protocol, create an iterator class named `PrimeIterator` that generates prime numbers from `1` to a number `n`, where `n` is greater than 1, which stops the iteration with the appropriate exception when it gets to a number greater than `n` 

(b) Redefine the `PrimeIterator` class above using the concept of generators by defining a generator function named `prime_generator` that accomplishes the same functionality

## Task 2

Define a decorator named `get_month_decorator`, that decorates a function named `get_month` which takes an integer between `1 & 12 (inclusive)` representing the month of the year and returns the month as a string.

**Example:** Given an input integer 9, the output string will be `"September"` Ensure to validate input strings.

The purpose of the decorator function(`get_month_decorator`) is to validate that the integer to be passed to the decorated function(`get_month`) is indeed an integer between `1 & 12 (inclusive)`, otherwise raise an `ArgumentError` exception with a nice error message. While the purpose of the decorated function (`get_month`) is simply to return the expected month string based on the valid month integer passed in as argument

## Task 3
Create a parent class named `Animal` and two child classes `Dog` and `Cat`. Each child class should inherit all the functionalities of the parent class and also have some methods unique to it.
This particular task is to test your understanding of classes and class structures.

