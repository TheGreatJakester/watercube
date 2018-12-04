#include "colors.inc"
#include "stones.inc"
#include "textures.inc"
#include "shapes.inc"
#include "glass.inc"
#include "metals.inc"
#include "woods.inc"


camera {
        location <5, 5, 20>
        look_at 0
}
background { color White } // to make the torus easy to see

light_source { <300, 300, -1000> White }

light_source { <6, 6, 25> White }

isosurface {
        function { sin(x)+ sin(z) + y }
        contained_by { box { -8, 8 } }
        texture{pigment{color Green}}
}

box{

        <-5,1,-5>
        <5,1.01,5>
        
}

box{

        <-5,2,-5>
        <5,2.01,5>
        
}

box{

        <-5,0,-5>
        <5,0.01,5>
        
}