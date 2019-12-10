from math import gcd, sin, cos, atan2, degrees, pi

map = [
"....#.....#.#...##..........#.......#......",
".....#...####..##...#......#.........#.....",
".#.#...#..........#.....#.##.......#...#..#",
".#..#...........#..#..#.#.......####.....#.",
"##..#.................#...#..........##.##.",
"#..##.#...#.....##.#..#...#..#..#....#....#",
"##...#.............#.#..........#...#.....#",
"#.#..##.#.#..#.#...#.....#.#.............#.",
"...#..##....#........#.....................",
"##....###..#.#.......#...#..........#..#..#",
"....#.#....##...###......#......#...#......",
".........#.#.....#..#........#..#..##..#...",
"....##...#..##...#.....##.#..#....#........",
"............#....######......##......#...#.",
"#...........##...#.#......#....#....#......",
"......#.....#.#....#...##.###.....#...#.#..",
"..#.....##..........#..........#...........",
"..#.#..#......#......#.....#...##.......##.",
".#..#....##......#.............#...........",
"..##.#.....#.........#....###.........#..#.",
"...#....#...#.#.......#...#.#.....#........",
"...####........#...#....#....#........##..#",
".#...........#.................#...#...#..#",
"#................#......#..#...........#..#",
"..#.#.......#...........#.#......#.........",
"....#............#.............#.####.#.#..",
".....##....#..#...........###........#...#.",
".#.....#...#.#...#..#..........#..#.#......",
".#.##...#........#..#...##...#...#...#.#.#.",
"#.......#...#...###..#....#..#...#.........",
".....#...##...#.###.#...##..........##.###.",
"..#.....#.##..#.....#..#.....#....#....#..#",
".....#.....#..............####.#.........#.",
"..#..#.#..#.....#..........#..#....#....#..",
"#.....#.#......##.....#...#...#.......#.#..",
"..##.##...........#..........#.............",
"...#..##....#...##..##......#........#....#",
".....#..........##.#.##..#....##..#........",
".#...#...#......#..#.##.....#...#.....##...",
"...##.#....#...........####.#....#.#....#..",
"...#....#.#..#.........#.......#..#...##...",
"...##..............#......#................",
"........................#....##..#........#"]

map_tiles = [[x for x in y] for y in map]

max_vis = (0,0,0)

def get_vectors(asteroid_x,asteroid_y,tiles):
    vectors = []
    for y in range(0,len(map_tiles)):
        for x in range(0,len(map_tiles[y])):
            if x == asteroid_x and y == asteroid_y:
                continue
            if tiles[y][x] == '#':
                x_diff = x-asteroid_x
                y_diff = y-asteroid_y
                if x_diff != 0 and y_diff != 0:
                    greatest_common_divisor = gcd(x_diff,y_diff)
                    vectors.append((int(x_diff/greatest_common_divisor),int(y_diff/greatest_common_divisor)))
                else:
                    vectors.append((x_diff if x_diff == 0 else 1 if x_diff > 0 else -1,y_diff if y_diff == 0 else 1 if y_diff > 0 else -1))
    return vectors

base = (30,34)

asteroids_destroyed = 0
last_destroyed = None
vectors_to_this_asteroid = get_vectors(base[0],base[1],map_tiles)
unique_vectors = set(vectors_to_this_asteroid)
angles = [(x[0],x[1],360+degrees((-1*pi/2)+atan2(x[0],x[1]))) for x in unique_vectors]
sorted_angles = sorted(angles, key=lambda x: -1*x[2])

while asteroids_destroyed < 200:
    for angle in sorted_angles:
        last_destroyed = (base[0]+angle[0],base[1]+angle[1])
        print(last_destroyed)
        map_tiles[base[1]+angle[1]][base[0]+angle[0]] = "."
        asteroids_destroyed = asteroids_destroyed + 1
        if asteroids_destroyed == 200:
            break
    vectors_to_this_asteroid = get_vectors(base[0],base[1],map_tiles)
    unique_vectors = set(vectors_to_this_asteroid)
    angles = [(x[0],x[1],360+degrees(atan2(x[0],x[1])) if degrees(atan2(x[0],x[1])) < 0 else degrees(atan2(x[0],x[1]))) for x in unique_vectors]
    sorted_angles = sorted(angles, key=lambda x: x[2])

print(last_destroyed[0]*100+last_destroyed[1])
