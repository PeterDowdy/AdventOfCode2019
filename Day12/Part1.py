moons = [(-16, -1, -12), (0, -4, -17), (-11, 11, 0), (2, 2, -6)]
velocities = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

def step():
    for i in range(0,4):
        moon = moons[i]
        gravity_delta = (sum([-1 if other_moon[0] < moon[0] else 1 if other_moon[0] > moon[0] else 0 for other_moon in moons]),
            sum([-1 if other_moon[1] < moon[1] else 1 if other_moon[1] > moon[1] else 0 for other_moon in moons]),
            sum([-1 if other_moon[2] < moon[2] else 1 if other_moon[2] > moon[2] else 0 for other_moon in moons])
        )
        velocity = velocities[i]
        velocities[i] = (velocity[0]+gravity_delta[0],velocity[1]+gravity_delta[1],velocity[2]+gravity_delta[2])
    for i in range(0,4):
        moon = moons[i]
        velocity = velocities[i]
        moons[i] = (moon[0]+velocity[0],moon[1]+velocity[1],moon[2]+velocity[2])

for i in range(0,1000):
    print(moons)
    print(velocities)
    step()

def potential_energy(x):
    return abs(x[0])+abs(x[1])+abs(x[2])

def kinetic_energy(x):
    return abs(x[0])+abs(x[1])+abs(x[2])

energy = 0
for i in range(0,4):
    energy += (potential_energy(moons[i])*kinetic_energy(velocities[i]))

print(energy)