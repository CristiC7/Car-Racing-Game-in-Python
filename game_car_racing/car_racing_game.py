import random  # Import the random module for generating random values
from time import sleep  # Import sleep function to pause the game for a short duration

import pygame  # Import the pygame library for game development
from pathlib2 import Path  # Import Path from pathlib2 to manage file paths

class CarRacing:
    def __init__(self):
        pygame.init()  # Initialize pygame
        self.display_width = 800  # Set the width of the game window
        self.display_height = 600  # Set the height of the game window
        self.black = (0, 0, 0)  # Define black color
        self.white = (255, 255, 255)  # Define white color
        self.clock = pygame.time.Clock()  # Create a clock object to control game speed
        self.gameDisplay = None  # Initialize game display
        self.root_path = str(Path(__file__).parent)  # Get the path to the current directory

        self.initialize()  # Call the initialization function

    def initialize(self):
        """Initialize game variables and assets."""
        self.crashed = False  # Game state flag

        # Load player's car image
        self.carImg = pygame.image.load(self.root_path + "/img/car.png")
        self.car_x_coordinate = (self.display_width * 0.45)  # Initial X position of the car
        self.car_y_coordinate = (self.display_height * 0.8)  # Initial Y position of the car
        self.car_width = 49  # Car width

        # Load enemy car image and set initial position and speed
        self.enemy_car = pygame.image.load(self.root_path + "/img/enemy_car_1.png")
        self.enemy_car_startx = random.randrange(310, 450)  # Random X position
        self.enemy_car_starty = -600  # Start off-screen
        self.enemy_car_speed = 5  # Initial speed
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        # Load background image
        self.bgImg = pygame.image.load(self.root_path + "/img/back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3  # Initial background scrolling speed
        self.count = 0  # Score counter

    def car(self, car_x_coordinate, car_y_coordinate):
        """Draw the player's car on the screen."""
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))

    def racing_window(self):
        """Create and display the game window."""
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Race by Cristi')  # Set window title
        self.run_car()  # Start the game loop

    def run_car(self):
        """Main game loop."""
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit event
                    self.crashed = True

                # Handle keypress events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.car_x_coordinate -= 50  # Move left
                        print("CAR X COORDINATES: %s" % self.car_x_coordinate)
                    if event.key == pygame.K_RIGHT:
                        self.car_x_coordinate += 50  # Move right
                        print("CAR X COORDINATES: %s" % self.car_x_coordinate)

            # Fill the screen with black background
            self.gameDisplay.fill(self.black)
            self.back_ground_road()  # Scroll the background

            # Move and display the enemy car
            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            # Reset enemy car position when it moves out of screen
            if self.enemy_car_starty > self.display_height:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(310, 450)

            # Draw player's car and update score
            self.car(self.car_x_coordinate, self.car_y_coordinate)
            self.highscore(self.count)
            self.count += 1  # Increment score

            # Increase speed at every 100 points
            if self.count % 100 == 0:
                self.enemy_car_speed += 1
                self.bg_speed += 1

            # Check for collision with enemy car
            if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or \
                   self.car_x_coordinate + self.car_width > self.enemy_car_startx and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                    self.crashed = True
                    self.display_message("Game Over !!!")

            # Check for collision with road boundaries
            if self.car_x_coordinate < 310 or self.car_x_coordinate > 460:
                self.crashed = True
                self.display_message("Game Over !!!")

            pygame.display.update()  # Refresh screen
            self.clock.tick(60)  # Limit frame rate

    def display_message(self, msg):
        """Display game over message and restart the game."""
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)  # Pause for 1 second before restarting
        car_racing.initialize()  # Reinitialize the game
        car_racing.racing_window()  # Restart the game

    def back_ground_road(self):
        """Animate the moving road background."""
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        # Move background downwards
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        # Reset background position when it moves out of screen
        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        """Draw the enemy car on the screen."""
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count):
        """Display the player's score."""
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        """Display credits on the screen."""
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Enjoy,", True, self.white)
        self.gameDisplay.blit(text, (600, 520))
        text = font.render("Cristi", True, self.white)
        self.gameDisplay.blit(text, (600, 540))

if __name__ == '__main__':
    car_racing = CarRacing()  # Create an instance of the game
    car_racing.racing_window()  # Start the game