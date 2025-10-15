import os
import pygame

# Setup environment for headless environments
if os.environ.get('DISPLAY'):
    print("No display detected. Using dummy video driver.")
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Initialize Pygame
try:
    pygame.mixer.init()
except:
    print("pygame mixer not initialized; using dummy driver.")
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
    pygame.mixer.quit()
    pygame.mixer.init()

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
except pygame.error:
    print("Unable to initialize display, running headless.")
    screen = pygame.Surface((WIDTH, HEIGHT))

pygame.display.set_caption("Gravity & Jumping Demo")

# Define a simple Player class
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 30
        self.height = 50
        self.color = (0, 255, 0)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_strength = 15
        self.on_ground = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        # Apply gravity
        gravity = 0.8
        self.vel_y += gravity
        self.x += self.vel_x
        self.y += self.vel_y

        # Keep within screen bounds
        if self.x < 0:
            self.x = 0
        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width

        # Floor collision
        if self.y + self.height >= HEIGHT:
            self.y = HEIGHT - self.height
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

# Setup game objects
player = Player()

# Create a simple floor as a Rect
floor_rect = pygame.Rect(0, HEIGHT - 20, WIDTH, 20)

# Create a door to switch rooms
class Door:
    def __init__(self, x, y, destination):
        self.rect = pygame.Rect(x, y, 70, 70)
        self.destination = destination

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

# Rooms with doors
class Room:
    def __init__(self, name):
        self.name = name
        self.doors = []

    def add_door(self, door):
        self.doors.append(door)

    def draw(self, surface):
        surface.fill((30, 30, 30))
        for door in self.doors:
            door.draw(surface)

    def get_door_at(self, x, y):
        for door in self.doors:
            if door.rect.collidepoint(x, y):
                return door
        return None

# Setup two rooms
room1 = Room('Room1')
room2 = Room('Room2')
door1 = Door(WIDTH - 80, HEIGHT//2 - 35, 'Room2')
door2 = Door(10, HEIGHT//2 - 35, 'Room1')
room1.add_door(door1)
room2.add_door(door2)

current_room = room1

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.vel_x = -player.speed
    elif keys[pygame.K_RIGHT]:
        player.vel_x = player.speed
    else:
        player.vel_x = 0

    if keys[pygame.K_SPACE]:
        if player.on_ground:
            player.vel_y = -player.jump_strength

    # Update player with gravity
    player.update()

    # Check for door collision
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    door = current_room.get_door_at(player.x + player.width/2, player.y + player.height/2)
    if door:
        current_room = room2 if door.destination == 'Room2' else room1
        # Reset player position
        player.x, player.y = 100, 100

    # Draw everything
    current_room.draw(screen)
    # Draw floor
    pygame.draw.rect(screen, (100, 100, 100), floor_rect)
    # Draw player
    player.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()