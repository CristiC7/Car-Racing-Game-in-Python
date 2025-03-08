# Car-Racing-Game-in-Python
This application is a simple car racing game developed with Pygame. The aim of the game is for the player to control a car that must avoid collision with an enemy car coming from the top of the screen. The game gets progressively more difficult by increasing speed as the player's score increases.

The game checks the collision between the player's car and the enemy car by comparing coordinates.
If the player hits the edges of the road (< 310 or > 460), the game ends.
As the player survives longer, the speed of the enemy car and the background increases, making the game more difficult.

Main code functionalities:

◆ Game Initialization:

The Pygame module is initialized.

Define the game window size (800x600).

Set the colors used (black, white).

Create a Clock object to control the game speed.

Load images for the player car, enemy car and background.

◆ Function initialize(self):

Initializes game variables, such as the initial position of the player car and the enemy car.

Sets the initial speed of the enemy car and background.

◆ Function racing_window(self):

Creates the game window and sets its title.

Calls the run_car() function to start the main game loop.

◆ Function run_car(self):

 • Represents the main game loop, where game events and logic are handled:

Detects if the player presses the left/right keys to move the car.

Updates the enemy car's position and checks for collisions.

Increases game speed as the score increases.

Stops the game and displays the "Game Over" message in case of a collision.

◆ Function display_message(self, msg):

Displays a message on the screen (e.g. "Game Over !!!") and restarts the game after a 1 second pause.

◆ Function back_ground_road(self)

Simulates the effect of moving the road by running the background from top to bottom.

◆ Function run_enemy_car(self, thingx, thingy)

Draws the enemy car on the screen and updates its position.

◆ Function highscore(self, count):

Displays the player's score in the top left corner of the screen.

◆ Function display_credit(self):

Displays a message with the name of the game developer.

◆ Running the game (if __name__ == '__main__')

Create an instance of the CarRacing class and start the game via racing_window().

◆ Future improvements:

• Adding a start menu and restart button.

• Introducing more enemy car types.

• Added a sound effect on collisions.

• Implemented a more complex progressive difficulty mechanic.
