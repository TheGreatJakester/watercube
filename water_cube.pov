#include "colors.inc"
#include "stones.inc"
#include "textures.inc"
#include "shapes.inc"
#include "glass.inc"
#include "metals.inc"
#include "woods.inc"

#declare still = false;

camera {
        location <sin(2*3.14*clock/40)*10, 8, cos(2*3.14*clock/40)*10>
        look_at <0,0,0>
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
    pigment{color rgb <.05,.05,.05>}
}

background { color Black }

#declare dist = function(xo,yo,xa,ya){
    pow(pow(yo-ya,2)+pow(xo-xa,2),.5)
}

#declare ripple = function(x_,amplitude,freq,wave_tip_dist,length){
        amplitude*
        sin((min(x_,wave_tip_dist)-wave_tip_dist)*freq)*
        max(0,((x_-wave_tip_dist)/length)+1)
}

#declare boat = union{
        box{
                <-2,0,-1>
                < 2,1, 1>
                texture{ Dark_Wood }
        }

        box{
                <-.5,1,-.5>
                <.5,1.5,.5>
                texture{ Dark_Wood }
        }
}

object{boat scale .5 rotate<sin(2*3.14*clock/15)*20,0,sin(2*3.14*clock/10)*5> translate <2,2.7,2>}

text {
ttf "timrom.ttf" "Jacob Moulton" .2, 0
texture { Cork }
rotate<90,180,sin(3.14*clock/15)*5>
translate<3,2.5,0>
}

box{
        <-4,0,-4> , <4,.001,4>
        texture{pigment{color rgb <.4,.4,.4>}}
}


#if(still)
isosurface {
        function{
                -3 + y
        }
        accuracy 0.0001
        contained_by { box { <-4,0,-4> , <4,3,4> } }
        texture{pigment{color Blue transmit 0.95}}
        interior { ior 1.1 }
        finish { reflection {.01}}
}
#else
isosurface {
        function{
                //#include "ripples.inc"
                ripple(dist(x,z,0,3),.08,10  ,max(clock-0,0),4) +
                ripple(dist(x,z,-3,3),.08,10 ,max(clock-10,0),4) +
                ripple(dist(x,z,0,1),.08,10  ,max(clock-15,0),4) +
                ripple(dist(x,z,-3,-1),.08,10,max(clock-22,0),4) +
                ripple(dist(x,z,-3,3),.08,10 ,max(clock-40,0),4) +
                ripple(dist(x,z,1,-3),.08,10 ,max(clock-45,0),4) +
                ripple(dist(x,z,3,-2),.08,10 ,max(clock-50,0),4) +
                ripple(dist(x,z,0,3),.08,10  ,max(clock-60,0),4) +
                ripple(dist(x,z,-3,-0),.08,10,max(clock-70,0),4) +
                ripple(dist(x,z,2,-3),.08,10 ,max(clock-75,0),4) +
                ripple(dist(x,z,1,1),.08,10  ,max(clock-80,0),4) +
                -3 + y
        }
        accuracy 0.001
        contained_by { box { <-4,0,-4> , <4,3,4> } }
        texture{pigment{color rgb <.3,.3,1> transmit 0.85}}
        interior { ior 1.1 }
        finish { reflection {.3}}
}
#end
