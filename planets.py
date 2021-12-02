GlowScript
3.2
VPython
e_graph = gcurve(color=color.blue)


def gforce(p1, p2):
    G = 1
    p_vec = p1.pos - p2.pos

    p_mag = mag(p_vec)

    p_dir = p_vec / p_mag

    force_mag = G * p1.mass * p2.mass / p_mag ** 2

    force_vec = -force_mag * p_dir

    return force_vec


star = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.green,
              mass=1000, momentum=vector(0, 0, 0), make_trail=True)

planet1 = sphere(pos=vector(1, 0, 0), radius=0.05, color=color.red,
                 mass=1, momentum=vector(0, 30, 0), make_trail=True)

planet2 = sphere(pos=vector(0, 3, 0), radius=0.075, color=color.blue,
                 mass=2, momentum=vector(-35, 0, 0), make_trail=True)

dt = 0.00005
t = 0
while (True):
    rate(1000)

    star.force = gforce(star, planet1) + gforce(star, planet2)
    planet1.force = gforce(planet1, star) + gforce(planet1, planet2)
    planet2.force = gforce(planet2, star) + gforce(planet2, planet1)

    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt

    star.pos = star.pos + star.momentum / star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum / planet1.mass * dt
    planet2.pos = planet2.pos + planet2.momentum / planet2.mass * dt

    t = t + dt
