import time
import machine
from neopixel import NeoPixel

# Configuration for WS2812
LED_PIN = 13  # Change this to the GPIO pin you're using
WIDTH = 16
HEIGHT = 16
NUM_PIXELS = WIDTH * HEIGHT
np = NeoPixel(machine.Pin(LED_PIN), NUM_PIXELS)

# Initialize ADC pins for joystick
x_axis = machine.ADC(machine.Pin(26))  # Connect to VRx
y_axis = machine.ADC(machine.Pin(27))  # Connect to VRy
joystick_button = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)

# Thresholds for joystick movement
DEADZONE = 1000  # Adjust based on your joystick's noise
CENTER = 32768   # Middle value for ADC (12-bit ADC values range from 0 to 65535)

def read_joystick():
    """Read the joystick and determine the direction."""
    global direction
    x_value = x_axis.read_u16()
    y_value = y_axis.read_u16()

    if abs(x_value - CENTER) > DEADZONE:
        if x_value > CENTER:  # Joystick pushed to the right
            direction = (1, 0)
        elif x_value < CENTER:  # Joystick pushed to the left
            direction = (-1, 0)

    if abs(y_value - CENTER) > DEADZONE:
        if y_value > CENTER:  # Joystick pushed down
            direction = (0, 1)
        elif y_value < CENTER:  # Joystick pushed up
            direction = (0, -1)

# Snake game variables
snake = [(8, 8)]  # Starting position
direction = (0, -1)  # Initial direction (UP)
food = (5, 5)
game_over = False

# Helper functions
def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        np[y * WIDTH + x] = color

def clear_matrix():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)

def draw_snake():
    for segment in snake:
        set_pixel(segment[0], segment[1], (0, 255, 0))  # Green for snake
    set_pixel(food[0], food[1], (255, 0, 0))  # Red for food
    np.write()

def move_snake():
    global game_over, food
    # Calculate new head position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Check collisions
    if (
        new_head in snake or  # Collide with itself
        not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)
    ):
        game_over = True
        return
    
    # Move snake
    snake.insert(0, new_head)
    
    if new_head == food:
        # Generate new food
        import random
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        # Remove tail
        snake.pop()

def update_direction():
    global direction
    if not up.value():
        direction = (0, -1)  # UP
    elif not down.value():
        direction = (0, 1)  # DOWN
    elif not left.value():
        direction = (-1, 0)  # LEFT
    elif not right.value():
        direction = (1, 0)  # RIGHT

# Main game loop
while not game_over:
    
    print('test')
    clear_matrix()
    read_joystick()  # Update direction based on joystick
    move_snake()
    draw_snake()
    time.sleep(0.2)

# Game Over
clear_matrix()
for i in range(3):
    for j in range(NUM_PIXELS):
        np[j] = (255, 0, 0)  # Flash red
    np.write()
    time.sleep(0.5)
    clear_matrix()
    np.write()
    time.sleep(0.5)

