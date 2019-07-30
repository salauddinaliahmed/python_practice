""" When you need to perform an operation multiple times until you reach the base case.
    Then you need take the result of the base case and start solving your problem bottom up.
"""
# The age old example. 
def fact(n):
    if n == 0:
        # Base case  
        return 1
    else:
        # general case.
        """
            Keeps calling itself until base case is reached, since we know the output of the base case. 
        """
        return n * fact(n-1)

# Failing to reach a base case can cause the system to crash. 
# Luckily most interpreters (like python) have a recurison limit of 1000 by default. This can be changed via the sys module.

print (fact(5)) 


#GCD recursion.
#Needed euclidean proof
"""
a, b
Say, a > b
formula => a = b * (some number) + remainder
next iteration. a = b
                b = remainder
"""

def gcd(num1,num2):
    a = max(num1, num2)
    b = min(num1, num2)
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print (gcd(10,15))
 
