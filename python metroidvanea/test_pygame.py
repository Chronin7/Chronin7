import os
import pygame
import time

# Initialize Pygame and handle sound issues
try:
    pygame.mixer.init()
except pygame.error:
    print("Using a codespace or pygame is not installed properly. Disabling sound.")
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
finally:
    pygame.init()
    pygame.mixer.init()

# Screen dimensions and setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("python metroidvanea")

# Load player image or use a default rectangle
try:
    player_image = pygame.image.load(r'P:\perl,liam\Chronin7\python metroidvanea\metroidvanea pngs and ohter files\player.png')
    player_image = pygame.transform.scale(player_image, (30, 60))
except pygame.error:
    print("Player image not found. Using a default rectangle.")
    player_image = pygame.Surface((30, 60))
    player_image.fill((255, 0, 0)) # Red rectangle

# Sound functions
def play_sound(track_path):
    try:
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
    except pygame.error:
        print("Music file not found or sound disabled.")

def stop_sound():
    pygame.mixer.music.stop()

# Consistent tile size
TILE_SIZE = 30

# Define classes for game elements
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

class Door:
    def __init__(self, x_grid, y_grid, destination, requirement=None):
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.destination = destination
        self.requirement = requirement
        self.rect = pygame.Rect(self.x_grid * TILE_SIZE, self.y_grid * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def can_open(self, player_items):
        if self.requirement is None:
            return True
        return self.requirement in player_items

class Room:
    def __init__(self, name, layout):
        self.name = name
        self.layout = layout
        self.room_width = len(self.layout[0]) * TILE_SIZE
        self.room_height = len(self.layout) * TILE_SIZE
        self.room_surface = pygame.Surface((self.room_width, self.room_height))
        self.walls = []
        self.doors = []
        self.entities = []

    def load_room(self, doors):
        self.walls = []
        self.doors = doors
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile == '#':
                    self.walls.append(Wall(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    def add_door(self, door):
        self.doors.append(door)

    def render(self, surface, scale_factor):
        self.room_surface.fill((0, 0, 0))
        for wall in self.walls:
            pygame.draw.rect(self.room_surface, (0, 255, 0), wall.rect)
        for door in self.doors:
            pygame.draw.rect(self.room_surface, (255, 255, 0), door.rect)
        for entity in self.entities:
            self.room_surface.blit(entity['image'], (entity['x'], entity['y']))
        
        scaled_room_surface = pygame.transform.scale(self.room_surface, (int(self.room_width * scale_factor), int(self.room_height * scale_factor)))
        
        offset_x = (SCREEN_WIDTH - scaled_room_surface.get_width()) // 2
        offset_y = (SCREEN_HEIGHT - scaled_room_surface.get_height()) // 2

        surface.blit(scaled_room_surface, (offset_x, offset_y))

    def get_door_at(self, player_rect):
        for door in self.doors:
            if player_rect.colliderect(door.rect):
                return door
        return None

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.player = {
            "x": 100,
            "y": 100,
            "width": 30,
            "height": 60,
            "image": player_image,
            "items": [],
            "rect": pygame.Rect(100, 100, 30, 60),
            "speed": 5,
            "y_velocity": 0,
            "is_jumping": False,
        }
        self.gravity = 1
        self.jump_strength = -15
        self.running = True
        
        self.scale_factor = min(SCREEN_WIDTH / (20 * TILE_SIZE), SCREEN_HEIGHT / (20 * TILE_SIZE))

    def add_room(self, room):
        self.rooms[room.name] = room

    def set_current_room(self, room_name, previous_room_name=None):
        self.current_room = self.rooms.get(room_name)
        if self.current_room:
            self.current_room.load_room(self.rooms.get(room_name).doors)
            
            if previous_room_name:
                for new_door in self.current_room.doors:
                    if new_door.destination == previous_room_name:
                        self.player['x'] = new_door.x_grid * TILE_SIZE + TILE_SIZE
                        self.player['y'] = new_door.y_grid * TILE_SIZE
                        break
            
            self.player['rect'].topleft = (self.player['x'], self.player['y'])

    def move(self, dx, dy):
        self.player['y_velocity'] += self.gravity
        if self.player['y_velocity'] > 10:
            self.player['y_velocity'] = 10
        
        self.player['x'] += dx
        self.player['rect'].x = self.player['x']
        for wall in self.current_room.walls:
            if self.player['rect'].colliderect(wall.rect):
                if dx > 0:
                    self.player['rect'].right = wall.rect.left
                if dx < 0:
                    self.player['rect'].left = wall.rect.right
                self.player['x'] = self.player['rect'].x

        self.player['y'] += dy + self.player['y_velocity']
        self.player['rect'].y = self.player['y']
        for wall in self.current_room.walls:
            if self.player['rect'].colliderect(wall.rect):
                if self.player['y_velocity'] > 0:
                    self.player['rect'].bottom = wall.rect.top
                    self.player['y_velocity'] = 0
                    self.player['is_jumping'] = False
                if self.player['y_velocity'] < 0:
                    self.player['rect'].top = wall.rect.bottom
                    self.player['y_velocity'] = 0
                self.player['y'] = self.player['rect'].y

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx -= self.player['speed']
        if keys[pygame.K_RIGHT]:
            dx += self.player['speed']
        if keys[pygame.K_UP] and not self.player['is_jumping']:
            self.player['is_jumping'] = True
            self.player['y_velocity'] = self.jump_strength
            
        self.move(dx, 0)
        
        if keys[pygame.K_ESCAPE]:
            self.running = False

    def check_for_door_and_transition(self):
        door = self.current_room.get_door_at(self.player['rect'])
        if door and door.can_open(self.player['items']):
            previous_room_name = self.current_room.name
            self.set_current_room(door.destination, previous_room_name=previous_room_name)

    def run(self):
        clock = pygame.time.Clock()
        try:
            play_sound(r'P:\perl,liam\Chronin7\python metroidvanea\metroidvanea pngs and ohter files\test.mp3')
        except FileNotFoundError:
            print("Music file 'test.mp3' not found.")
            
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.handle_input()
            self.check_for_door_and_transition()
            
            self.current_room.render(screen, self.scale_factor)
            
            scaled_player_rect = pygame.Rect(
                self.player['x'] * self.scale_factor,
                self.player['y'] * self.scale_factor,
                self.player['width'] * self.scale_factor,
                self.player['height'] * self.scale_factor
            )
            scaled_player_image = pygame.transform.scale(self.player['image'], scaled_player_rect.size)
            
            offset_x = (SCREEN_WIDTH - self.current_room.room_width * self.scale_factor) // 2
            offset_y = (SCREEN_HEIGHT - self.current_room.room_height * self.scale_factor) // 2
            
            screen.blit(scaled_player_image, (scaled_player_rect.x + offset_x, scaled_player_rect.y + offset_y))
            
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

# Setup game environment with example rooms
def setup_game():
    game = Game()
    
    main_room_layout = [
        "####################",
        "#                  #",
        "#                  #",
        "#                  #",
        "#                  #",
        "#                  #",
        "#            #     #",
        "#D          #  #   #",
        "#          #       #",
        "####################",
    ]

    main_room = Room("MainRoom", main_room_layout)
    main_room.add_door(Door(1, 7, "ItemRoom"))
    game.add_room(main_room)
    
    item_room_layout = [
        "##########",
        "#        #",
        "#        #",
        "#        #",
        "#       D#",
        "##########",
    ]
    
    item_room = Room("ItemRoom", item_room_layout)
    item_room.add_door(Door(8, 4, "MainRoom"))
    game.add_room(item_room)
    
    game.set_current_room("MainRoom")
    return game

if __name__ == "__main__":
    game = setup_game()
    game.run()
