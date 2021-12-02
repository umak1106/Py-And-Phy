GlowScript 3.2 VPython
ground=box(pos=vector(0,-.2,0),size=vector(20,.4,2),color=color.blue)
ball=sphere(pos=vector(-10,1.1,0),radius=.1, color=color.green, make_trail=True)
r0=ball.pos
g=vector(0,-9.8,0)
ball.m=0.2
v0=20
theta=75*pi/180
ball.p=ball.m*v0*vector(cos(theta),sin(theta),0)

t=0
dt=0.004

while ball.pos.y>=0.1:
  rate(100)
  Fnet=ball.m*g
  ball.p=ball.p+Fnet*dt
  ball.pos=ball.pos+ball.p*dt/ball.m
  t=t+dt

print("dr final = ",ball.pos-r0," m")
print("t final = ",t," s")
