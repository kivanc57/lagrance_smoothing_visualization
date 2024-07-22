from copy import deepcopy

def set_lagrance(any_list, special_indexes):
    new_list = deepcopy(any_list)
    max_i = len(any_list)

    for i in special_indexes:
        total = []
        #Check the neighbours if they are not BORDERs and ZEROs,
        #If not, add to list 'total' to calculate later

        y, x = i[0], i[1]
        # Check left neighbour
        if (x != 0) and (x % max_i != 0) and (any_list[y][x-1] != 0):
            total.append(any_list[y][x-1])

        # Check right neighbour
        if ((x + 1) % max_i != 0) and (any_list[y][x+1] != 0):
            total.append(any_list[y][x+1])

        # Check upper neighbour
        if (y != 0) and any_list[y-1][x] != 0:
            total.append(any_list[y-1][x])

        # Check lower neighbour
        if (y + 1 !=  max_i) and any_list[y+1][x] != 0:
            total.append(any_list[y+1][x])

        # Replace the element by the sum divided by length and round it to one decimal
        if len(total) > 0:
            new_list[y][x] = round(sum(total) / len(total), 1)

    return new_list, special_indexes
