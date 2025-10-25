# # closure is when we have access of a local variable and data of another function to another function and remember it
# def outer():
#     message = "hi"
#     def inner():
#         print(message) # using a variable which was not created in this function (this is closure)
#     return inner # here we are remembring and passing that function's value to inner function and can use whenever we want

# my_work = outer()
# print(my_work()) # using the closure value (i.e inner function having access to the outer funciton vaiables even after being executed)


from functools import wraps, update_wrapper

def greet(func): # we are creating a decorator function which will take a funciton to decorate it
    @wraps(func) # using it to wrap the function to preserve the orignal data
    def wrapper(*args): # as we will be accepting arguments we will use that
        print("Welcome")
        result = func(*args) # adding functionallity to a function with out changing its original functionality 
        print(result)
        print("BYE")
        return result
    return wrapper # like this we are returning that wrapper which will be assigned to a var and then we can access it


# we can access it as
@greet # like this we can use a decorator to another funciton
def square(x):
    return x ** 2

# ans = square(2)
# print(ans)


# we can aslo create a decorator by using CLASS instead function

class NewGreet:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)
    
    def __call__(self, *args, **kwds):
        print("Before the function")
        print(self.func(*args, **kwds))
        print( "After the function")
        return self.func(*args, **kwds)

@NewGreet
def cube(x):
    return x ** 3

# cube(2)


# if we have a function where there we are using two or multiple decorators we need to set the decorator as it will not give us the expected result

# we can do it by impoting a module called functools and using it wraps 

@greet
@NewGreet
def fourth(x):
    return x ** 4

fourth(2)