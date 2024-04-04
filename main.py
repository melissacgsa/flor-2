from turtle import *
import colorsys

tracer(100)
bgcolor('white')
pensize(25)
h = 0.10
up()
goto(-150, 0)
down()

for i in range(480):
  c = colorsys. hsv_to_rgb (h , 0.4, 0.4)
  h += 0.001
  color(c)
  up(), circle(i, 20)
  down(), circle(80, 145)
  lt(141)

done()
