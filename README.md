# Lagrance Smoothing Visualization

## Overview

**Lagrance Smoothing Visualization** is a Python-based application designed to generate a random game map, apply Lagrance smoothing to adjacent numerical values, and visualize the process at each step. The application provides an interactive way to understand the smoothing algorithm and its effects on the data.

## Features

- **Game Map Generation:** Creates a game map with random values and specified missing values.
- **Lagrance Smoothing:** Applies Lagrance smoothing to adjust the missing values based on their neighbors.
- **Visualization:** Visualizes the game map at each step of the smoothing process.

## Installation
1. **Clone the repository**: 
    ```bash
    git clone https://github.com/yourusername/lagrance_smoothing_visualization.git
    
    ```

2. **Navigate to the project directory**:  
    ```bash
    cd cd lagrance_smoothing_visualization
    
    ```

3. **Install any required dependencies (if applicable)**.
    ```bash
    pip install -r requirements.txt
    
    ```

## Usage  
1. Ensure you have Python 3.x installed.

2. Run the application by executing:
    ```bash
    python main.py
    ```
3. Follow the on-screen prompts to observe the Lagrance smoothing process and visualize the game map.

# Project Structure
```markdown
📁 project-root
├── 📁 config
│ ├── 📄 init.py
│ └── 📄 constants.py
│
├── 📁 src
│ ├── 📄 init.py
│ ├── 📄 generate_map.py
│ ├── 📄 lagrance_smoothing.py
│ └── 📄 visualization.py
│
├── 📄 .gitattributes
├── 📄 .gitignore
└── 📄 main.py
```
- **config/**: Contains configuration files.
  - ***\__init__.py***: Imports constants for game configuration.
  - ***constants.py***: Defines constants used throughout the application.

- **src/**: Contains source code files.
  - ***\__init__.py***: Initializes the source package, sets up logging, and imports main functions and constants.
  - ***generate_map.py***: Generates the initial game map with random values and missing values.
  - ***lagrance_smoothing.py***: Applies Lagrance smoothing to the game map.
  - ***visualization.py***: Visualizes the game map at each step of the smoothing process.

- ***.gitattributes***: Ensures consistent line endings across different operating systems in the repository.

- ***.gitignore***: Specifies files and directories to be ignored by Git (e.g., virtual environments, build artifacts).

## Code Examples
### Main Program
**main.py**: The entry point of the application. Initializes settings, generates the game map, applies Lagrance smoothing, and visualizes the process.

```python

from numpy import allclose
from src.generate_map import get_map
from src.lagrance_smoothing import set_lagrance
from src.visualization import make_image
from config.constants import SIDE_LENGTH, MISSING_VALUES, TOLERANCE, STEP_LIMIT_MULTIPLIER

def main():
    side_length = SIDE_LENGTH
    missing_values = MISSING_VALUES
    step_limit_multiplier = STEP_LIMIT_MULTIPLIER
    tolerance = TOLERANCE

    random_map, indexes = get_map(side_length, missing_values)
    make_image(random_map) #Visualize the first map with missing values
    step_limit = len(indexes) * step_limit_multiplier + 1
    for step in range(1, step_limit):  # Limit the number of steps to avoid infinite loop
        print(f"This is STEP: {step}")
        new_map, indexes = set_lagrance(random_map, indexes)
        make_image(new_map) #Visualize current map
        # Check if the arrays are almost equal (within a small tolerance)
        if allclose(new_map, random_map, atol=tolerance):
            print(f"No more changes! Final STEP: {step}")
            break

        random_map = new_map

if __name__ == '__main__':
    main()
```


### Generate Map
```python
from src.generate_map import get_map

side_length = 4
missing_values = 4
random_map, indexes = get_map(side_length, missing_values)
print(random_map)
print(indexes)

```

### Apply Lagrance Smoothing
```python
from src.lagrance_smoothing import set_lagrance

new_map, indexes = set_lagrance(random_map, indexes)
print(new_map)

```

## Visualize Map
```python
from src.visualization import make_image

make_image(new_map)

```

## Contact
Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024
