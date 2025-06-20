import random

class Snake:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position

    def move(self, direction):
        head_x, head_y = self.positions[0]
        new_head_position = (head_x + direction[0] * self.BLOCK_SIZE, head_y + direction[1] * self.BLOCK_SIZE)
        
        if new_head_position == self.food_position:
            self.eat_food()
        else:
            self.positions.pop()

        if new_head_position in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new_head_position)

    def random_food_position(self):
        while True:
            x = random.randint(0, (self.SCREEN_WIDTH // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE
            y = random.randint(0, (self.SCREEN_HEIGHT // self.BLOCK_SIZE) - 1) * self.BLOCK_SIZE
            food_position = (x, y)
            if food_position not in self.positions:
                self.food_position = food_position
                break

    def reset(self):
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        self.length += 1
        self.score += 10
        self.positions.append(self.positions[-1])
        self.random_food_position()