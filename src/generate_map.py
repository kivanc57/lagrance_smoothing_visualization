from random import choices

def get_map(side_length, missing_values):
    game_map = list()
    special_indexes = list()

    #Create the sides with random values between 1 and 9
    for _ in range(side_length):
        row = [float(value) for value in choices(range(1, side_length), k=side_length)]
        game_map.append(row)
    
    #Adjust missing values as 0s to the game map and store their values in special_indexes
    for _ in range(missing_values):
        i_coordinates = tuple(choices(range(side_length), k=2)) #Mutuability is not desired, convert list to tuple.
        game_map[i_coordinates[0]][i_coordinates[1]] = 0.0
        special_indexes.append(i_coordinates)
    return game_map, special_indexes
