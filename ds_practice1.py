from random import randint

def sal_shuffle(l):
    value_holder = []
    # Use the randint function to mimic shuffle.
    while True:
        # Create a list of random values.
        random_val = randint(0, (len(l)-1))
        if not random_val in value_holder:
            value_holder.append(random_val)

        if len(value_holder) == len(l):
            break
    new_l = [0 for _ in range(len(value_holder))]
    for index, each_element in enumerate(l):
        new_l[value_holder[index]] = l[index]
    
    print ("Shuffled list:", new_l)

sal_shuffle([1,2,4,5,6])