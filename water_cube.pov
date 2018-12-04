#include "colors.inc"
#include "stones.inc"
#include "textures.inc"
#include "shapes.inc"
#include "glass.inc"
#include "metals.inc"
#include "woods.inc"

#declare wave_speed=10;

camera {
        location <0, 3, 5>
        look_at 0
}
light_source{
        <6,6,6> color White
        }
light_source
{ <0,0,0> color 1
  looks_like
  { sphere
    { <0,0,0>,0.1
      color White 
      finish { ambient 1 }
    }
  }
  translate <0,20,0>
  spotlight
  radius 15
  falloff 50
  tightness 20
  point_at <0,0,0>
}

plane {
    <0,1,0>, -1
    pigment{checker color Black, color White}
}

background { color Black } // to make the torus easy to see

#declare dist = function(xo,yo,xa,ya){
    pow(pow(yo-ya,2)+pow(xo-xa,2),.5)
}

#declare ripple = function(x_,amplitude,freq,wave_tip_dist,length){
        amplitude*
        sin((min(x_,wave_tip_dist)-wave_tip_dist)*freq)*
        max(0,((x_-wave_tip_dist)/length)+1)
}


isosurface {
        function{
                ripple(dist(x,z,5,5),.08,10,4+clock*wave_speed,2) + 
        y
        }
        contained_by { box { -2, 2 } }
        texture{pigment{color Blue transmit 0.85}}
        interior { ior 1.5 }
        finish { reflection {.5}}
}
