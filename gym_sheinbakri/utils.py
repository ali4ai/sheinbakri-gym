# utils.py

def get_cell_from_position(x, y, cell_size):
    """ Convert pixel coordinates to grid coordinates """
    return x // cell_size, y // cell_size

def is_within_bounds(position, grid_size):
    """ Check if a position is within the board limits """
    row, col = position
    return 0 <= row < grid_size and 0 <= col < grid_size

def manhattan_distance(pos1, pos2):
    """ Calculate Manhattan distance between two positions """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
