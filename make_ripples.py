ripple_template = "ripple(dist(x,z,{},{}),.08,10,4+clock*wave_speed,2)"
class Ripple:
    def __init__(self,p):
        self.position = p

    def __eq__(self,other):
        return self.position[0] == other.position[0] and self.position[1] == self.position[1]
    def to_string(self):
        return ripple_template.format(self.position[0],self.position[1])

    #determines which of 9 regions this point resides in. 
    #Determines what walls it bounces off.
    def region(self,x1,x2,y1,y2):
        if self.position[1] >= y2:
            if self.position[0] <= x1:
                return 4
            elif self.position[0] > x1 and self.position[0] < x2:
                return 3
            elif self.position[0] >= x2:
                return 2
        elif self.position[1] < y2 and self.position[1] > y1:
            if self.position[0] <= x1:
                return 5
            elif self.position[0] > x1 and self.position[0] < x2:
                return 0
            elif self.position[0] >= x2:
                return 1
        elif self.position[1] <= y1:
            if self.position[0] <= x1:
                return 6
            elif self.position[0] > x1 and self.position[0] < x2:
                return 7
            elif self.position[0] >= x2:
                return 8   
    #returns all the ripples that would take effect when the ripples bounce off walls
    #as defined by the corners.
    def reflect_helper (self,a,z):
        return 2*z - a

    def reflect_x(self,x):
        position = (self.reflect_helper(self.position[0],x),self.position[1])
        return Ripple(position)

    def reflect_y(self,y):
        return Ripple((
            self.position[0],
            self.reflect_helper(self.position[1],y)
        ))

    def reflect(self,x1,x2,y1,y2):
        reflected_ripples = []
        region = self.region(x1,x2,y1,y2)
        if region == 0 :
            reflected_ripples.append(self.reflect_x(x1))
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 1 :
            reflected_ripples.append(self.reflect_x(x1))
            reflected_ripples.append(self.reflect_y(y1))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 2 :
            reflected_ripples.append(self.reflect_x(x1))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 3 :
            reflected_ripples.append(self.reflect_x(x1))
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 4 :
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 5 :
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 6 :
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 7 :
            reflected_ripples.append(self.reflect_x(x1))
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))
        elif region == 8 :
            reflected_ripples.append(self.reflect_x(x2))
            reflected_ripples.append(self.reflect_y(y1))

        return reflected_ripples


depth = 10

ripples = []
to_do_ripples = []
first_ripple = Ripple((-1,-1))
to_do_ripples.append(first_ripple)

for i in range(depth):
    doing = []
    doing.extend(to_do_ripples)
    ripples.extend(to_do_ripples)
    to_do_ripples.clear()
    for Ripple in doing:
        to_do_ripples.extend(Ripple.reflect(-4,4,-4,4))



buffer = ""
for ripple in ripples:
    buffer += ripple.to_string() + "\n\t\t"

ripple_file = open("ripples.inc","w")
ripple_file.write(buffer)
ripple_file.close()
