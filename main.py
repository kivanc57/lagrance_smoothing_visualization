# How general principle works: 
# *Generate the game map
# *Perform Lagrance smoothing on adjacent numerical values
# *Visualize it

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
