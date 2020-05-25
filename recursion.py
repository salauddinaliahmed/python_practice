<<<<<<< HEAD
def draw_line(tick_length, label=""):
    line = '-' * tick_length
    if label:
        line += " " + label
    print(line)

def draw_interval(central_length):
    if central_length>0:
        print ("Executed", central_length)
        draw_interval(central_length-1)
        print ("drawing", central_length)
        draw_line(central_length)
        print ("Drawn", central_length)
        draw_interval(central_length-1)
        print ("Reaced here", central_length)

def draw_ruler(num_inches, length_ticks):
    draw_line(length_ticks, '0')
    for i in range(1, 1 + num_inches):
        draw_interval(length_ticks-1)
        draw_line(length_ticks, str(i))

draw_ruler(4,3)


=======
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
 

"""This an example of string palindrome"""

def stringpalin(stro):
    stro = stro.split(" ")
    lent = len(stro)
    if lent == 1:
        return stro[0]
    else:
        A = ' '.join(stro[0:lent-1])
        return stro[-1]+ " " + stringpalin(' '.join(stro[0:lent-1]))

print (stringpalin("Can it print a long sentence in reverse? Lets put it to test"))



"""
    The main idea behind recursion is that you need to boil down to one or more base cases and build your way up. 
    In the solution provided on stack overflow(Brilliant answer by ssm). he was checking each element of includes list with the word. Thw word
    remained of the same length but the search word changed.

    SO, think in terms of both directs. Can we change the input or can we manipulate the condition such that i can 
    test the whole case. 
    
    Lesson learnt.
"""

def checkstring(word, includes):
    if includes == '':
        return includes in word
    else:
        #Check from the first word and keep adding the result. 
        #The base case is always true.
        #In the recursive portion, you are doing most of your logical operations.
        return (includes[0] in word) and checkstring(word,includes[1:])

print (checkstring("Whiteleaf", "elf"))


# another recursion problem dealing with reversing string with O(n/2) time.
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        stop = len(s)
        
        
        def helper(start, stop):
            if start == stop:
                s[start] = s[stop]
            elif stop-start >= 1:
                s[start], s[stop] = s[stop], s[start]
                return helper(start+1, stop-1)
            
        helper(start,stop-1)

x = Solution()
s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
x.reverseString(s)
print (s)
>>>>>>> 462bf76681fba8b7a677b4ef6f77839c1f6fd681

