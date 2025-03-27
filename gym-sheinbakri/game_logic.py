# game_logic.py

class GameLogic:
    def __init__(self):
        self.grid_size = 7
        self.tiger_position = (3, 3)  # Initial position of the Tiger
        self.goat_positions = set()
        self.goats_placed = 0
        self.max_goats = 15
        self.current_turn = 'goat'  # Goat moves first
    
    def is_valid_move(self, piece, start_pos, end_pos):
        """ Check if the move is valid """
        if piece == 'tiger':
            return self.is_valid_tiger_move(start_pos, end_pos)
        elif piece == 'goat':
            return self.is_valid_goat_move(start_pos, end_pos)
        return False
    
    def is_valid_tiger_move(self, start_pos, end_pos):
        """ Tigers can move one step or jump over a goat """
        row_diff = abs(start_pos[0] - end_pos[0])
        col_diff = abs(start_pos[1] - end_pos[1])
        return (row_diff <= 2 and col_diff <= 2)  # Simple logic, will refine later
    
    def is_valid_goat_move(self, start_pos, end_pos):
        """ Goats can move one step in any direction """
        row_diff = abs(start_pos[0] - end_pos[0])
        col_diff = abs(start_pos[1] - end_pos[1])
        return (row_diff == 1 and col_diff == 1)
    
    def place_goat(self, position):
        """ Place a goat on the board """
        if self.goats_placed < self.max_goats and position not in self.goat_positions:
            self.goat_positions.add(position)
            self.goats_placed += 1
            return True
        return False
    
    def move_piece(self, piece, start_pos, end_pos):
        """ Move a piece if the move is valid """
        if self.is_valid_move(piece, start_pos, end_pos):
            if piece == 'tiger':
                self.tiger_position = end_pos
            elif piece == 'goat':
                self.goat_positions.remove(start_pos)
                self.goat_positions.add(end_pos)
            return True
        return False
    
    def check_win_condition(self):
        """ Check if the game is won by either player """
        if len(self.goat_positions) < 5:  # Example win condition
            return 'tiger'
        if self.tiger_position in self.goat_positions:  # Example condition for trapping the tiger
            return 'goat'
        return None
