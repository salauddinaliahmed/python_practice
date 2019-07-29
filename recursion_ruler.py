"""

Sample output:

---
-
--
-
---

steps that i know:
interval = 1 less than total ticks
* Every inch has 2 intervals, one before and one after the actual half. (remeber, when we pass the draw_interval, we are actually reducing the size by 1)
Therefore, the steps involved are as such:
Length provided actually 3 ticks.
Length passed to the function => (3-1) = 2

****
Algo:

Basic :
The basic structure of the rule is as follows,
1. Draw line with number of ticks
2. Draw interval, which is the length of ticks-1
3. Draw line with the number of ticks.

But, we uncover that if the number of ticks increase, there are more complex patterns (fractals) building inside. Each inch, has an internal draw_interval.
Now, the catch is that each draw interval will need to have a specific set of steps. (This is the actual algorithm design)

Inside a draw_interval:
1. Each interval has the first length one less than the interval passed. -> This needs to be recursively called until we get to the most basic of the intervals. (which is one.)
   Thus, keeping the condition greater than 0. Also, <  (serves as a base case returning None)
2. Draw, line which is the interval length passed by the recursively called draw_interval 
3. Then draw the interval of one less than passed value.

eg: 
'-' length = 3
---
-
--
-
---

draws line ---
calls interval (2)
    calls interval(1)
    draw(2)
    draw_interval(1)
        draw_interval(0)
    print (1)             ----------
    draw(line with n = 1)        \
    calls interval(1)   
        intern calls draw interval(0)-None          \
        calls interval(0)          \
            Returns None ----------

Why? Look for the pattern.
So, there is a pattern inside every interval.
    1. Draw interval of (length passed - 1). 
       

draw_line -> Draws single tick with specified number of lines. 
draw_interval -> is recursively called. (Important)=> Draws sequence of minor ticks within some interval.
(based on the length of the interval's central tick)

# Base case -> L=0 draws nothing.
"""
#draw line function draws a line with passed ticks.
def draw_line(ticks):
    print ('-'*ticks)

#The core logic of recursion.
def draw_interval(center):
    # if center > 0, then we can move ahead with drawing.
    if center > 0:
        draw_interval(center - 1)
        draw_line(center)
        draw_interval(center - 1)

def ruler(inches, ticks):
    # Each series of recursion will produce output for one inch. 
    # Draw first line
    draw_line(ticks)
    for i in range(inches):
        #draw the first line. 
        #Now, the next line contains ticks which is one less than the original ticks
        draw_interval(ticks-1)
        # now end the dashed line sequence.
        draw_line(ticks)

ruler(1,4)
