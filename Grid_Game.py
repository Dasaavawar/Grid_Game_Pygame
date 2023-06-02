import pygame
import sys
import random

# Define the size of the grid
rows = 12
cols = 12

# Define the size of each grid cell
cell_size = 50

# Define the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Create the window
window_width = cols * cell_size
window_height = rows * cell_size
window = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("Grid Game")

# Create an empty grid
grid = [['-' for _ in range(cols)] for _ in range(rows)]

# Class representing a person
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def draw(self):
        person_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, RED, person_rect)

    def move(self, dx, dy):
        if not self.alive:
            return
        else:
            new_x = self.x + dx
            new_y = self.y + dy

        # Check if the new position is within the grid boundaries
        if 0 <= new_x < cols and 0 <= new_y < rows:
            if grid[new_y][new_x] == 'P':
                self.alive = False
                print("You fell into a pitfall!")
            elif grid[new_y][new_x] == 'T':
                print("You collided with a tree!")
            elif grid[new_y][new_x] == 'E':
                print("You collided with another person!")
            else:
                self.x = new_x
                self.y = new_y

# Class representing a pitfall
class Pitfall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pitfall_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, BLUE, pitfall_rect)

# Class representing a tree
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        tree_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, GREEN, tree_rect)

# Create a person objects
person1 = Person(0, 0)
person2 = Person(5, 6)
person3 = Person(7, 3)

# Add person objects to a list
persons = [person1, person2, person3]

# Place persons in the grid
grid[person1.y][person1.x] = 'E'
grid[person2.y][person2.x] = 'E'
grid[person3.y][person3.x] = 'E'

# Create a pitfall objects
pitfall1 = Pitfall(1, 2)
pitfall2 = Pitfall(3, 4)
pitfall3 = Pitfall(4, 10)
pitfall4 = Pitfall(5, 6)

# Place pitfall objects in the grid
grid[pitfall1.y][pitfall1.x] = 'P'
grid[pitfall2.y][pitfall2.x] = 'P'
grid[pitfall3.y][pitfall3.x] = 'P'
grid[pitfall4.y][pitfall4.x] = 'P'

# Create tree objects randomly placed on grid borders
trees = []
for _ in range(10):
    x = random.choice([0, cols - 1])
    y = random.randint(0, rows - 1)
    tree = Tree(x, y)
    trees.append(tree)
    grid[y][x] = 'T'

# Function to draw the grid
def draw_grid():
    for row in range(rows):
        for col in range(cols):
            cell_x = col * cell_size
            cell_y = row * cell_size
            pygame.draw.rect(window, WHITE, (cell_x, cell_y, cell_size, cell_size), 1)
            if grid[row][col] == 'P':
                pitfall = Pitfall(col, row)
                pitfall.draw()
            elif grid[row][col] == 'T':
                tree = Tree(col, row)
                tree.draw()
            elif grid[row][col] == 'E':
                for person in persons:
                    if person.x == col and person.y == row and person.alive:
                        person.draw()

# Function to update the display
def update_display():
    window.fill(BLACK)
    draw_grid()
    pitfall1.draw()
    pitfall2.draw()
    if person1.alive:
        person1.draw()
    elif not person1.alive:
        grid[person1.y][person1.x] = None
    if person2.alive:
        person2.draw()
    elif not person2.alive:
        grid[person2.y][person2.x] = None
    if person3.alive:
        person3.draw()
    elif not person3.alive:
        grid[person3.y][person3.x] = None
    if (not person1.alive and not person2.alive and not person3.alive):
        print('Game over')
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                person1.move(0, -1)
                person2.move(0, -1)
                person3.move(0, -1)
            elif event.key == pygame.K_DOWN:
                person1.move(0, 1)
                person2.move(0, 1)
                person3.move(0, 1)
            elif event.key == pygame.K_LEFT:
                person1.move(-1, 0)
                person2.move(-1, 0)
                person3.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                person1.move(1, 0)
                person2.move(1, 0)
                person3.move(1, 0)

    # Update the display
    update_display()

# Quit the game
pygame.quit()
sys.exit()
