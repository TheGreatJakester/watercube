ripple_template = "\t\tripple(dist(x,z,{},{}),.08,10,clock,4) +\n"

def reflect_x(point,x):
    return (2*x - point[0],point[1])

def reflect_y(point,y):
    return (point[0],2*y-point[1])

def reflect(point,x1,x2,y1,y2):
    region = -1
    reflected_ripples = []
    if point[1] >= y2:
        if point[0] <= x1:
            region =  4
        elif point[0] > x1 and point[0] < x2:
            region =  3
        elif point[0] >= x2:
            region =  2
    elif point[1] < y2 and point[1] > y1:
        if point[0] <= x1:
            region =  5
        elif point[0] > x1 and point[0] < x2:
            region =  0
        elif point[0] >= x2:
            region =  1
    elif point[1] <= y1:
        if point[0] <= x1:
            region =  6
        elif point[0] > x1 and point[0] < x2:
            region =  7
        elif point[0] >= x2:
            region =  8
    
    if region == 0 :
        reflected_ripples.append(reflect_x(point,x1))
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 1 :
        reflected_ripples.append(reflect_x(point,x1))
        reflected_ripples.append(reflect_y(point,y1))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 2 :
        reflected_ripples.append(reflect_x(point,x1))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 3 :
        reflected_ripples.append(reflect_x(point,x1))
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 4 :
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 5 :
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 6 :
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 7 :
        reflected_ripples.append(reflect_x(point,x1))
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))
    elif region == 8 :
        reflected_ripples.append(reflect_x(point,x2))
        reflected_ripples.append(reflect_y(point,y1))

    return reflected_ripples


x1 = -4
x2 =  4
y1 = -4
y2 =  4

initial = (3,3)

ripples = []
to_do = [] 
to_do.append(initial)

depth = 4

buffer = ""
if_start = "#if (clock > {} && clock < {})\n"

reflect_time = 12
margin = 3

for i in range(depth):
    doing = []
    doing.extend(to_do)
    ripples.extend(to_do)
    to_do.clear()

    #buffer += if_start.format(reflect_time*i-margin,reflect_time*(i+1)+margin)
    for ripple in doing:
        buffer += ripple_template.format(*ripple)
        to_do.extend(reflect(ripple,x1,x2,y1,y2))
    #buffer += "#end\n"

ripple_file = open("ripples.inc","w")
ripple_file.write(buffer)
ripple_file.close()