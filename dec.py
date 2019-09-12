def uppercase_decorator(function):
    print ("Entered outer decorator function")
    def wrapper():
        print ("Control is in inner function")
        func = function()
        print("control after function call from inner function")
        make_uppercase = func.upper()
        return make_uppercase
    print ("Calling wrapper now")
    return wrapper

def say_hi():
    print ("Control is in say hi function")
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print (decorate())