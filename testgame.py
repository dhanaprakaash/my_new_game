import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Robot Simulation')

# Define robot parameters
robot_radius = 20
robot_color = (255, 0, 0)
robot_position = [width // 2, height // 2]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the robot (in this example, simply move in a circle)
    robot_position[0] += 1
    if robot_position[0] > width:
        robot_position[0] = 0

    # Draw the robot
    screen.fill((255, 255, 255))  # Clear the screen
    pygame.draw.circle(screen, robot_color, (int(robot_position[0]), int(robot_position[1])), robot_radius)

    pygame.display.flip()  # Update the display
    pygame.time.Clock().tick(60)  # Cap the frame rate

