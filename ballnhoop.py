

count = 0

g = -9.8
Position = vec(0, 17.75, 40)

ground = box(pos=vec(0, 0, 0), length=80, height=2, width=95)

scene.camera.pos = vec(0, 15, 0)
pole = cylinder(pos=vec(0, 1, -15), axis=vec(0, 20, 0), radius=1, color=color.yellow)
pole2 = cylinder(pos=vec(0, 20, -15), axis=vec(0, 7, 10), radius=1, color=color.yellow)
board = box(pos=vec(0, 28, -4), length=15, height=10, width=0.5, color=color.yellow)
goal = ring(pos=vec(0, 23.75, -2), axis=vec(0, 1, 0), radius=2.5, thickness=0.15, color=color.red)
mylabel = label(pos=vec(0, 50, 0))
mylabel.text = count
welcome = label(pos=vec(0, 60, 0))
welcome.text = " Shoot!"
ball = sphere(pos=Position, radius=1.5, color=color.orange)
ball.m = 0.155
ball.angle = 36 * pi / 180
ball.speed = -22
ball.v = ball.speed * vec(0, -cos(ball.angle), sin(ball.angle))

t = 0
dt = 0.007

scene.waitfor('click')
while (1):
    rate(1000)

    grav = ball.m * vec(0, g, 0)

    ball.f = grav

    ball.v = ball.v + ball.f / ball.m * dt
    ball.pos = ball.pos + ball.v * dt

    if ball.pos.y - ball.radius < 0:
        ball.v.y = -0.71 * ball.v.y
        count = count + 1
        ball.pos = Position
        bounce = 0
        scene.waitfor('click')

    mylabel.text = count
    t = t + dt

