import pyautogui
import webbrowser
import time
import math

# Open the website in your default web browser
webbrowser.open("https://neal.fun/perfect-circle/")

# Wait for the webpage to load (you may need to adjust the wait time)
time.sleep(1)

# Get the center point of the screen
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

# Move the mouse to the center of the screen and press the left mouse button
pyautogui.moveTo(center_x, center_y)
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.mouseUp()


# Define the circle parameters
radius = 470
num_points = 60  # Number of points to create a circle
first = True
# Draw a circle by moving the mouse around the center point
for angle in range(0, 360, 360 // num_points):
    x = center_x + int(radius * math.cos(math.radians(angle)))
    y = center_y + int(radius * math.sin(math.radians(angle)))
    pyautogui.moveTo(x, y)
    if first == True:
        pyautogui.mouseDown()
        first = False


pyautogui.mouseUp()

