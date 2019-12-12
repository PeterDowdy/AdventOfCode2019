from math import gcd

moons = [(-16, -1, -12), (0, -4, -17), (-11, 11, 0), (2, 2, -6)]
velocities = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

x_positions = set()
y_positions = set()
z_positions = set()

x_positions.add((moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0]))
y_positions.add((moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][2],velocities[2][1],velocities[3][1]))
z_positions.add((moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][0],velocities[2][2],velocities[3][2]))

x_sequences = {(moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0]): 0}
y_sequences = {(moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][1],velocities[2][1],velocities[3][1]): 0}
z_sequences = {(moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][2],velocities[2][2],velocities[3][2]): 0}

ctr = 0
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



x_cycle_length = 0
y_cycle_length = 0
z_cycle_length = 0

while True:
    ctr += 1
    step()
    if (moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0]) in x_positions:
        x_cycle_length = ctr-x_sequences[(moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0])]
        pass
    if (moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][2],velocities[2][1],velocities[3][1]) in y_positions:
        y_cycle_length = ctr-y_sequences[(moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][2],velocities[2][1],velocities[3][1])]
        pass
    if (moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][0],velocities[2][2],velocities[3][2]) in z_positions:
        z_cycle_length = ctr-z_sequences[(moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][0],velocities[2][2],velocities[3][2])]
        pass
    if x_cycle_length != 0 and y_cycle_length != 0 and z_cycle_length != 0:
        break
    x_positions.add((moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0]))
    y_positions.add((moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][2],velocities[2][1],velocities[3][1]))
    z_positions.add((moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][0],velocities[2][2],velocities[3][2]))
    x_sequences[(moons[0][0],moons[1][0],moons[2][0],moons[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0])] = ctr
    y_sequences[(moons[0][1],moons[1][1],moons[2][1],moons[3][1],velocities[0][1],velocities[1][2],velocities[2][1],velocities[3][1])] = ctr
    z_sequences[(moons[0][2],moons[1][2],moons[2][2],moons[3][2],velocities[0][2],velocities[1][0],velocities[2][2],velocities[3][2])] = ctr

print('Cycles found:')
print(f'x lasts {x_cycle_length}')
print(f'y lasts {y_cycle_length}')
print(f'z lasts {z_cycle_length}')

print((x_cycle_length,y_cycle_length,z_cycle_length))

def compute_lcm(x, y):
   return (x*y)/gcd(x,y)

print(int(compute_lcm(x_cycle_length, int(compute_lcm(y_cycle_length, z_cycle_length)))))
