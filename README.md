# Bloons TD Battles Custom Hotkey Script

## Overview
This repository contains a custom hotkey setup for the game Bloons TD Battles. The script is designed to enhance gameplay by remapping various game actions to more convenient and accessible keyboard keys. It also includes specialized macros for common game actions.

## Features
- **Top Row (Powers)**: Keys 'q', 'w', 'e' mapped to Powers 1, 2, 3.
- **Middle Row (Towers)**: Keys 'a', 's', 'd', 'f' mapped to Towers 1, 2, 3, and 4 (optional).
- **Special Macros**:
  - 'r': Sell (mapped to 'backspace').
  - 't': Upgrade Left (mapped to ',').
  - 'g': Upgrade Right (mapped to '.').
  - 'c': Upgrade Left fully, then Right (mapped to ',,,,..').
  - 'v': Upgrade Right fully, then Left (mapped to '....,,').
  - 'esc': Stop the script.
  - 'tab': Toggle tower focus (default mapped to 'tab').

## Installation and Usage
To use this script, follow the steps below:

### Cloning the Repository
1. Open your terminal.
2. Clone the repository to your local machine:
   ```
   git clone https://github.com/TheCyberLocal/bloons-td-battles-hotkeys
   ```
3. Navigate to the repository's directory:
   ```
   cd bloons-td-battles-hotkeys
   ```

### Installing Dependencies
1.  Must have QWERTY keyboard layout.
2.  This script requires Python and the `pynput` library. Make sure Python is installed on your system. Then, install the `pynput` library using pip:
```
pip install pynput
```

### Running the Script
1. Start Bloons TD Battles.
2. Run the script:
   ```
   python main.py
   ```
3. The script will listen for the specified hotkeys and execute the corresponding actions. Press 'esc' to stop the script.

## Note
Please ensure you comply with Bloons TD Battles' terms of service when using this script, particularly regarding the use of macros.

