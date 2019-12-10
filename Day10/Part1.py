from math import gcd

map = ["....#.....#.#...##..........#.......#......",
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


for y in range(0,len(map_tiles)):
    for x in range(0,len(map_tiles[y])):
        if map_tiles[y][x] == '.':
            continue
        vectors_to_this_asteroid = get_vectors(x,y,map_tiles)
        unique_vectors = set(vectors_to_this_asteroid)
        visible = len(unique_vectors)
        if visible > max_vis[2]:
            max_vis = (x,y,visible)

print(f'max visible: {max_vis[2]} at ({max_vis[0]},{max_vis[1]})')