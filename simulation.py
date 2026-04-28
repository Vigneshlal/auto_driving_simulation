class Car:
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = list(commands)
        self.active = True

    def turn_left(self):
        idx = Car.directions.index(self.direction)
        self.direction = Car.directions[(idx - 1) % 4]

    def turn_right(self):
        idx = Car.directions.index(self.direction)
        self.direction = Car.directions[(idx + 1) % 4]

    def move_forward(self, width, height):
        if self.direction == 'N' and self.y < height - 1:
            self.y += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'E' and self.x < width - 1:
            self.x += 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1
        # else: ignore move beyond boundary

    def step(self, width, height):
        if not self.commands or not self.active:
            return
        cmd = self.commands.pop(0)
        if cmd == 'L':
            self.turn_left()
        elif cmd == 'R':
            self.turn_right()
        elif cmd == 'F':
            self.move_forward(width, height)


def run_simulation(width, height, cars):
    positions = {}
    step = 0
    while any(c.active and c.commands for c in cars):
        step += 1
        for car in cars:
            if car.active and car.commands:
                car.step(width, height)
                pos = (car.x, car.y)
                if pos in positions:
                    other = positions[pos]
                    car.active = False
                    other.active = False
                    print(f"{car.name} collides with {other.name} at {pos} at step {step}")
                else:
                    positions[pos] = car
    return [(c.name, c.x, c.y, c.direction) for c in cars]
