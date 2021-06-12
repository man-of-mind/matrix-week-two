class PrimeIterator:
    def __init__(self, number):
        self.number = number


    def __iter__(self):
        self.num = 2
        return self


    def __next__(self):
        if self.num == 2:
            result = 2
            self.num += 1
            return result
        if self.num <= self.number:
            prime_num = False
            for j in range(2, self.num):
                if(self.num % j == 0):
                    prime_num  = False
                    self.num += 1
                prime_num = True
            if prime_num:
                result = self.num
                self.num += 1
                if result <= self.number:
                    return result

        raise StopIteration



"""This is the code for the generator with the functionality as above"""

def prime_generator(n):
    #this makes 2 to always be return first whatever the input value of n assuming it n is always greater than 1 
    if n >= 2:
        yield 2
    #then we check for prime condition from 3 to the last value which is n
    for num in range(3, n + 1):
        is_prime = False
        #check whether num is divible by any number between 2 and the number
        for i in range(2, num):
            if (num % i == 0):
                is_prime = False
                break
            is_prime = True
        if is_prime:
            yield num


user_input = input("Enter number: ")
try:
    if int(user_input) < 2:
        raise Exception('Enter a number greater than 1')
    else:
        print("Using generator, the prime number between 1 and {} are".format(user_input))
        for val in prime_generator(int(user_input)):
            print(val)
        prime = PrimeIterator(int(user_input))
        values = iter(prime)
        print("****Using iterator****")
        print(list(values))
except ValueError:
    print('The number must be a valid integer')
