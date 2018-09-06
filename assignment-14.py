
#Question1: Write a python program to print the cube of each value of a list using list comprehension.
liist=[10,11,97,10,5,98,30,3,98]
list1=[i**3 for i in liist]
print(list1)
print()

#Question2: Write a python program to get all the prime numbers in a specific range using list comprehension.
lower_limit,upper_limit=2,40
list2=[num for num in range(lower_limit,upper_limit) if all(num % y != 0 for y in range(2, num))]
print(list2)
print()

'''Question3: Write the main differences between List Comprehension and Generator Expression.
#LIST COMPREHENSION: list comprehensions allow you to create lists with a for loop with less code.

The comprehensions are not limited to lists.
You can create dicts and sets comprehensions as well.

GENERATOR EXPRESSION:->Generator is an iterable created using a function with a yield statement. 

The main feature of generator is evaluating the elements on demand.
When you call a normal function with a return statement the function
is terminated whenever it encounters a return statement.
In a function with a yield statement the state of the function is
“saved” from the last call and can be picked up the next time you
call a generator function.'''

#LAMBDA AND MAP

#Question1: Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
lst1=list(map(lambda c:c*1.8+32,Celsius))
print(lst1)
print()

#Question2: Apply an anonymous function to square all the elements of a list using map and lambda.
lst_=[1,2,3,4,5,6,7,8,9,12]
lst2=list(map(lambda x:x**2,lst_))
print(lst2)
print()

#FILTER AND REDUCE

#Question1: Filter out all the primes from a list.
def prime(a):
    for i in range(2,a):
        if (a % i) == 0:
            return False
        else:
            return True
lst__=[11,12,32,23,68,53]
f=list(filter(prime,lst__))
print(f)
print()

#Question2: Write a python program to multiply all the elements of a list using reduce.
from functools import *
lsst2=[1,2,3,4,5,6,7,8]
output=reduce(lambda x,y:x*y ,lsst2)
print(output)
print()
