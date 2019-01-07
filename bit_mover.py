import random
from sense_hat import SenseHat
from time import sleep
import array

sense = SenseHat()

sense.set_rotation(180)
x= []
y= []

#sense.show_message("Merry Christmas!")
x0=0
y0=0

for i in range(2): 
    for ypos in range(0,8):
       for xpos in range(0,8):
	  
      
        sense.set_pixel(x0,y0,0,0,0)

        #xpos=random.randint(0,7)
        #ypos=random.randint(0,7)

        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)

        x0=xpos
        y0=ypos

        sense.set_pixel(xpos,ypos,red,green,blue)
        sleep(0.1)

sense.set_pixel(x0,y0,0,0,0)
