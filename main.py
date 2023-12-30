"""
Bloons TD Battles Custom Hotkey Script

This script creates a custom hotkey setup for Bloons TD Battles,
 designed to enhance gameplay through ergonomic key remapping and specialized macros.
It maps various game actions to keyboard keys that are more accessible and convenient to use during gameplay.

Hotkeys and Macros:
- Top Row (Powers): Keys 'q', 'w', 'e' are mapped to Powers 1, 2, 3 respectively.
- Middle Row (Towers): Keys 'a', 's', 'd', 'f' are mapped to Towers 1, 2, 3, and 4 (optional) respectively.
- Special Macros:
  - 'r': Sell (mapped to 'backspace')
  - 't': Upgrade Left (mapped to ',')
  - 'g': Upgrade Right (mapped to '.')
  - 'c': Upgrade Left fully, then Right (mapped to ',,,,..')
  - 'v': Upgrade Right fully, then Left (mapped to '....,,')
  - 'esc': Stop the script
  - 'tab': Toggle tower focus (already mapped to 'tab')

Usage:
Run this script before starting Bloons TD Battles.
The script will listen for the specified hotkeys and execute the corresponding actions.
Press 'esc' to stop the script.

Note:
Ensure you comply with Bloons TD Battles' terms of service when using this script,
 particularly regarding the use of macros.
"""


# Import required libraries
from pynput import keyboard
from pynput.keyboard import Key, Controller
from time import sleep

# Initialize the keyboard controller
keyboard_controller = Controller()


# Define the hotkey listener
def on_press(key):
    try:
        # Power keys
        if key.char == 'q':

            print("Q was pressed, simulating 5: Use first power")

            # Simulate pressing and releasing the '5' key with a delay of 0.05 seconds
            keyboard_controller.press('5')
            sleep(0.05)
            keyboard_controller.release('5')

        elif key.char == 'w':

            print("W was pressed, simulating 6: Use second power")

            # Simulate pressing and releasing the '6' key with a delay of 0.05 seconds
            keyboard_controller.press('6')
            sleep(0.05)
            keyboard_controller.release('6')

        elif key.char == 'e':

            print("E was pressed, simulating 7: Use third power")

            # Simulate pressing and releasing the '7' key with a delay of 0.05 seconds
            keyboard_controller.press('7')
            sleep(0.05)
            keyboard_controller.release('7')

        # Tower keys
        elif key.char == 'a':

            print("A was pressed, simulating 1: Use first tower")

            # Simulate pressing and releasing the '1' key with a delay of 0.05 seconds
            keyboard_controller.press('1')
            sleep(0.05)
            keyboard_controller.release('1')

        elif key.char == 's':

            print("S was pressed, simulating 2: Use second tower")

            # Simulate pressing and releasing the '2' key with a delay of 0.05 seconds
            keyboard_controller.press('2')
            sleep(0.05)
            keyboard_controller.release('2')

        elif key.char == 'd':

            print("D was pressed, simulating 3: Use third tower")

            # Simulate pressing and releasing the '3' key with a delay of 0.05 seconds
            keyboard_controller.press('3')
            sleep(0.05)
            keyboard_controller.release('3')

        elif key.char == 'f':

            print("F was pressed, simulating 4: Use fourth tower")

            # Simulate pressing and releasing the '4' key with a delay of 0.05 seconds
            keyboard_controller.press('4')
            sleep(0.05)
            keyboard_controller.release('4')

        # Special keys
        elif key.char == 'r':

            print("R was pressed, simulating backspace: Sell tower")

            # Simulate pressing and releasing the 'backspace' key with a delay of 0.05 seconds
            keyboard_controller.press(Key.backspace)
            sleep(0.05)
            keyboard_controller.release(Key.backspace)

        elif key.char == 't':

            print("T was pressed, simulating ,: Upgrade tower left")

            # Simulate pressing and releasing the ',' key with a delay of 0.05 seconds
            keyboard_controller.press(',')
            sleep(0.05)
            keyboard_controller.release(',')

        elif key.char == 'g':

            print("G was pressed, simulating .: Upgrade tower right")

            # Simulate pressing and releasing the '.' key with a delay of 0.05 seconds
            keyboard_controller.press('.')
            sleep(0.05)
            keyboard_controller.release('.')

        elif key.char == 'c':

            print("C was pressed, simulating ,,,,..: Upgrade fully left then right macro")

            # Press ',' 4 times to upgrade left side fully
            for _ in range(4):
                keyboard_controller.press(',')
                sleep(0.05)
                keyboard_controller.release(',')

            # Press '.' 2 times to upgrade right side the rest of the way
            for _ in range(2):
                keyboard_controller.press('.')
                sleep(0.05)
                keyboard_controller.release('.')

        elif key.char == 'v':

            print("V was pressed, simulating ....,,: Upgrade fully right then left macro")

            # Press '.' 4 times to upgrade right side fully
            for _ in range(4):
                keyboard_controller.press('.')
                sleep(0.05)
                keyboard_controller.release('.')

            # Press ',' 2 times to upgrade left side the rest of the way
            for _ in range(2):
                keyboard_controller.press(',')
                sleep(0.05)
                keyboard_controller.release(',')

    except AttributeError:
        # Ignore special keys
        pass


def on_release(key):
    if key == Key.esc:
        # Stop listener if 'esc' is pressed
        return False


# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener
    listener.join()
