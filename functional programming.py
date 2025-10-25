# there are three methods of functional programing

# MAP
# it takes an iterable and run the function on each item of that iterable
list_1 = [1, 2, 3, 4]
square_of_list = list(map(lambda x : x * x, list_1)) # will perform that function on every item

print(square_of_list)


# FILTER
# filter is used to filter items out of iterable and pass them to another obj if its true

evens = list(filter(lambda x : x % 2 == 0, square_of_list ))
print(evens)

# REDUCE
# this is not a built in function so we use functools module to import this and use
# this will perform a functions on an iterable and will give a single value

from functools import reduce

sum_of_list = reduce(lambda x , y : x + y, evens)
print(sum_of_list)