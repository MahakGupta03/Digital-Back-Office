# list of all 4 directions
direction = ['N', 'E', 'S', 'W']
# movement of rovers, 1 grid point
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
# commands sent to rovers
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

class Rover:

    def __init__(self, x, y, xmax, ymax, facing, intersection):

        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.facing = facing
        self.intersection = set(intersection)

    def turn_right(self):
        """
        for turning right
        """
        self.facing = direction[(direction.index(self.facing) + 1) % len(direction)]

    def turn_left(self):
        """
        for turning left
        """
        self.facing = direction[(direction.index(self.facing) - 1) % len(direction)]

    def move(self):
        """
        move forward by 1 grid point
        """
        xmod = self.x + move[self.facing][0]
        ymod = self.y + move[self.facing][1]
        # check if 2 or more rovers are not at same position 
        if (xmod, ymod) not in self.intersection:
            #check if rovers are within the grid
            if xmod <= self.xmax and xmod >= 0:
                self.x = xmod
            if ymod <= self.ymax and ymod >= 0:
                self.y = ymod
            else:
                raise ValueError('Invalid move: rover out of bounds')
        else:
            raise ValueError('Invalid move: colliding with another rover')


if __name__ == '__main__':
    # get rover count
    rover_count = int(input("Enter rover count: "))

    # get input for grid
    xmax, ymax = map(int, input('grid size (eg: 5 5):').split())

    # initialise intersection rovers soon to be positions
    intersection = set([])
    check_position = []
    results = []

    # r is used to loop for rover count
    r = 1
    # c is used to loop for commands
    c = 1

    # iterate over rover count
    for _ in range(rover_count):

        # get coordinates for rover and direction the rover is facing
        x, y, facing = input(f'Coordinates for rover {r} (eg: 1 2 N):').split()
        r += 1

        # check if you havent deployed rovers with the same coordinates
        if [x, y, facing] not in check_position:
            check_position.append([x, y, facing])
            rover = Rover(int(x), int(y), xmax, ymax, facing, intersection)

            # iterate over commands string
            for i in input(f'Commands for rover {c} (eg: LMLMMM):'):
                if i not in 'MRL':
                    # exit if not valid instruction
                    raise ValueError(f'Invalid command: {i}')
                else:
                    # store and run commands
                    getattr(rover, commands[i])()
            c += 1
            # add rovers coordinates to intersection and update result
            intersection.add((rover.x, rover.y))
            results.append((rover.x, rover.y, rover.facing))
        else:
            raise ValueError('2 or more than 2 rover share the same spot')
        
    # print results
    for x, y, z in results:
        print(x, y, z)