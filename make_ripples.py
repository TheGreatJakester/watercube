ripple_template = "ripple(dist(x,z,{},{}),.08,10,4+clock*wave_speed,2)"
class ripple:
    def __init__(self,position):
        self.position = position
    def to_string(self):
        return ripple_template.format(self.position[0],self.position[1])

    #determines which of 9 regions this point resides in. 
    #Determines what walls it bounces off.
    def region(self,x1,x2,y1,y2):
        if self.position[1] >= y2:
            if self.position[0] <= x1:
                return 4
            elif self.position[0] > x1 or self.position[0] < x2:
                return 3
            elif self.position[0] >= x2:
                return 2
        elif self.position[1] < y2 or self.position[1] > y1:
            if self.position[0] <= x1:
                return 5
            elif self.position[0] > x1 or self.position[0] < x2:
                return 0
            elif self.position[0] >= x2:
                return 1
        elif self.position[1] <= y1:
            if self.position[0] <= x1:
                return 6
            elif self.position[0] > x1 or self.position[0] < x2:
                return 7
            elif self.position[0] >= x2:
                return 8   
    #returns all the ripples that would take effect when the ripples bounce off walls
    #as defined by the corners.
    def reflect(self,x1,x2,z1,z2):
        pass