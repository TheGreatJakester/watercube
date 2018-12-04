#include "colors.inc"
#include "stones.inc"
#include "textures.inc"
#include "shapes.inc"
#include "glass.inc"
#include "metals.inc"
#include "woods.inc"


camera {
        location <5, 25, 20>
        look_at 0
}
background { color White } // to make the torus easy to see

light_source { <0, 30, 0> White }

isosurface {
        function{ 
        sin((pow(pow(x   ,2)+pow(z   ,2),.5) - (pi*2)*clock)*2)*.25 +
        sin((pow(pow(x+10,2)+pow(z+10,2),.5) - (pi*2)*clock)*2)*.25 +
        y}
        
        contained_by { box { -80, 80 } }
        texture{pigment{color Blue transmit 0.95}}
        interior { ior 1.5 }
}


box{

        <-80,-4   ,-80>
        < 80,-4.01, 80>
        
        texture{pigment{color <.95,.95,1>}}
        
}
