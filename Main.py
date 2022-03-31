# We will make a program to find AREA of any Circle.

# For that User have to give the RADIUS of the Circle.

# So Area of Circle = π r²

import math

Pie = 22/7
Radius = float(input("Radius of the Circle\n"))
Unit = " sq. cm"


Area = (Pie * ((Radius * Radius )))


print(str(Area) + Unit)