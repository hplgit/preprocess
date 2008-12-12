c23456789012345678901234567890123456789012345678901234567890123456789012

      PROGRAM sphere

c  This program determines the surface area and volume of a sphere, given 
c  its radius.

c  Variable declarations
      REAL  rad, area, volume, pi

c  Definition of variables
c   rad = radius, area = surface area, volume = volume of the sphere

c  Assign a value to the variable pi.
      pi = 3.141593

c  Input the value of the radius and echo the inputted value.
      PRINT *, 'Enter the radius of the sphere.'
      READ *, rad
      PRINT *, rad, ' is the value of the radius.'

c  Compute the surface area and volume of the sphere.
      area = 4.0 * pi * rad**2
      volume = (4.0/3.0) * pi * rad**3

c  Print the values of the radius (given in cm), the surface area (sq cm),
c  and the volume (cubic cm).
      PRINT *,'In a sphere of radius', rad, ' , the surface area is',
     +          area, ' and its volume is', volume, '.'
      STOP

      END


