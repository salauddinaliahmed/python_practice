people = {
    'person1': {
        'name': 'Sally Sue',
        'city': 'Phoenix'
    },
    'person2': {
        'name': 'Billy Bob',
        'city': 'Scottsdale'
    },
    'person3': {
        'name': 'Rover',
        'city': 'Zappa'
    }
}

# Will try to use recursion here.
class Person:
    class Man:
        def __init__(self, name):
            self._called = name
            print ("Man", type(name))
    
    def make_man(self, p):
        return self.Man(self)

    def _validate(self, p):
        print ("Type of object passed: ", type(p))
        print ("This is the self instance",type(self)) 
        print ("First check", isinstance(p, self.Man))
        if p._called is self:
            print ("P_called type is this:, ", type(self))
        return None

x = Person()
a = x.make_man("Steve")
x._validate(a)
print (a.is_empty())
