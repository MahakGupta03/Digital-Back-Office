import unittest
from rover import Rover

class TestRover(unittest.TestCase):

    def test_turn_right(self):
        rover = Rover(0, 0, 5, 5, 'N', set())
        rover.turn_right()
        self.assertEqual((rover.x,rover.y,rover.facing), (0,0,'E'))

    def test_turn_left(self):
        rover = Rover(0, 0, 5, 5, 'N', set())
        rover.turn_left()
        self.assertEqual((rover.x,rover.y,rover.facing), (0,0,'W'))

    def test_move(self):
        rover = Rover(0, 0, 5, 5, 'N', set())
        rover.move()
        self.assertEqual((rover.x,rover.y,rover.facing), (0,1,'N'))

    def test_invalid_move_out_of_bounds(self):
        rover = Rover(5, 5, 5, 5, 'N', set())
        with self.assertRaises(ValueError):
            rover.move()

    def test_invalid_move_collision(self):
        intersection = {(5, 6)}
        rover = Rover(5, 5, 5, 5, 'N', intersection)
        with self.assertRaises(ValueError):
            rover.move()

    def test_multiple_commands(self):
        rover = Rover(1, 2, 5, 5, 'N', set())
        commands = 'LMLMLMLMM'
        for command in commands:
            if command == 'M':
                rover.move()
            elif command == 'R':
                rover.turn_right()
            elif command == 'L':
                rover.turn_left()
        self.assertEqual((rover.x, rover.y, rover.facing), (1, 3, 'N'))

        
    def test_out_of_bounds_commands(self):
        rover = Rover(5, 5, 5, 5, 'N', set())
        commands = 'MMMM'
        with self.assertRaises(ValueError):
            for command in commands:
                if command == 'M':
                    rover.move()

if __name__ == '__main__':
    unittest.main()
