class Plateau:
    def __init__(self, width, height, radius=None):
        self.width = width
        self.height = height
        self.radius = radius

    def within_boundaries(self, x, y):
        if self.radius is not None:
            return x**2 + y**2 <= self.radius**2   # Circular plateau, always within boundaries
        else:
            return 0 <= x <= self.width and 0 <= y <= self.height

class Rover:
    def __init__(self, x, y, plateau, facing):
        self.x = x
        self.y = y
        self.plateau = plateau
        self.facing = facing
        self.initial_x = x
        self.initial_y = y
        self.initial_facing = facing

    def reset_position(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.facing = self.initial_facing

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.facing)
        self.facing = directions[(current_index + 1) % len(directions)]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.facing)
        self.facing = directions[(current_index + 1) % len(directions)]

    def move(self):
        move_map = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        x, y = move_map[self.facing]
        new_x, new_y = self.x + x, self.y + y
        if self.plateau.within_boundaries(new_x, new_y):
            self.x, self.y = new_x, new_y
        else:
            raise ValueError('Invalid move: rover out of plateau boundaries')

if __name__ == '__main__':
    plateau_type = input("Enter the plateau type (circular or grid): ")
    if plateau_type.lower() == 'circular':
        radius = float(input("Enter the radius of the circular plateau: "))
        plateau = Plateau(None, None, radius)
    elif plateau_type.lower() == 'grid':
        width, height = map(int, input("Enter the width and height of the grid (eg: 5 5): ").split())
        plateau = Plateau(width, height)
    else:
        print("Invalid plateau type. Please enter 'circular' or 'grid'.")
        exit()

    rover_count = int(input("Enter rover count: "))
    rovers = []

    temp_rover_count = 0
    for i in range(rover_count):
        # temp_rover_count +=1 
        x, y, facing = input(f'Enter coordinates for rover {i+1} (eg: 1 2 N): ').split()
        if plateau.within_boundaries(int(x), int(y)):
            rover = Rover(int(x), int(y), plateau, facing)
            rovers.append((rover))
            while(temp_rover_count<=i):
                commands = input(f'Enter commands for rover {i+1} (eg: LMLMLMLMM): ')
                for command in commands:
                    if command not in 'MRL':
                        print(f'Resetting position for rover {rover.x} {rover.y} {rover.facing}')
                        rover.reset_position()
                        temp_rover_count -=1
                        continue
                    elif command == 'L':
                        rover.turn_left()
                    elif command == 'R':
                        rover.turn_right()
                    elif command == 'M':
                        rover.move()
                       
                temp_rover_count +=1
                
                    
        else:
            raise ValueError('Invalid move: rover out of plateau boundaries')

    for rover in rovers:
        print(f'Rover position: {rover.x} {rover.y} {rover.facing}')
