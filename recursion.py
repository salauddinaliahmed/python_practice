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



