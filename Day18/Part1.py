
map = [[y for y in x if y != '\n'] for x in open('Day18/input.txt').readlines()]
tiles = {}
for y in range(0,len(map)):
    for x in range(0,len(map[0])):
        tiles[(x,y)] = map[y][x]
pass

keys = list(set([v.lower() for k,v in tiles.items() if v not in ['#','.','@']]))
doors = list(set([v.upper() for k,v in tiles.items() if v not in ['#','.','@']]))

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end, keys_collected):
    # copied with modifications from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = {}
    closed_list = {}

    # Add the start node
    open_list[start_node.position]  = start_node

    width = max([k[0] for k,v in maze.items()])
    height = max([k[0] for k,v in maze.items()])
    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_key, current_node = next(iter(open_list.items()))
        for k,v in open_list.items():
            if v.f < current_node.f:
                current_node = v
                current_key = k

        # Pop current off open list, add to closed list
        open_list.pop(current_key)
        closed_list[current_node.position]=current_node

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > width or node_position[0] < 0 or node_position[1] > height or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[(node_position[0],node_position[1])] == '#' or(maze[(node_position[0],node_position[1])] in doors and maze[(node_position[0],node_position[1])].lower() not in keys_collected):
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if child.position in open_list:
                continue

            # Add the child to the open list
            open_list[child.position] = child

global shortest
shortest = 999999
current = [k for k,v in tiles.items() if v == '@'][0]
def key_search(map, current, keys_collected):
    global shortest
    if len(current) > shortest:
        return []
    searches = []
    if len(keys_collected) == 26:
        if len(current) < shortest:
            shortest = len(current)
        return [current]
    key_paths = []
    for key in keys:
        if key in keys_collected:
            continue
        key_paths.append((key,astar(tiles, current[-1], [k for k,v in tiles.items() if v == key][0], keys_collected)))
        key_paths = [x for x in key_paths if x[1] is not None]
    for path in key_paths:
        searches += key_search(map, current + path[1][1:], keys_collected + [path[0]])
    return searches

all_searches = key_search(tiles,[current],[])

print(all_searches)
print([len(x) for x in all_searches])