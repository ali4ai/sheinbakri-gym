# sheinbakri_env.py
import gym
import numpy as np
from gym import spaces
from gym_sheinbakri.game_logic import GameLogic
from gym_sheinbakri.render import Renderer

class SheinBakriEnv(gym.Env):
    def __init__(self):
        super(SheinBakriEnv, self).__init__()
        
        self.game = GameLogic()
        self.renderer = Renderer(self.game)
        
        self.observation_space = spaces.Box(low=0, high=1, shape=(7, 7, 2), dtype=np.int8)
        self.action_space = spaces.Discrete(49)  # 7x7 grid positions
        
    def reset(self):
        self.game = GameLogic()
        return self._get_observation()
    
    def step(self, action):
        row, col = divmod(action, 7)
        done = False
        reward = 0
        
        if self.game.current_turn == 'goat':
            if self.game.place_goat((row, col)):
                self.game.current_turn = 'tiger'
        else:
            if self.game.move_piece('tiger', self.game.tiger_position, (row, col)):
                self.game.current_turn = 'goat'
        
        winner = self.game.check_win_condition()
        if winner:
            done = True
            reward = 1 if winner == 'goat' else -1
        
        return self._get_observation(), reward, done, {}
    
    def render(self, mode='human'):
        self.renderer.render()
    
    def _get_observation(self):
        obs = np.zeros((7, 7, 2), dtype=np.int8)
        obs[self.game.tiger_position[0], self.game.tiger_position[1], 0] = 1
        for goat in self.game.goat_positions:
            obs[goat[0], goat[1], 1] = 1
        return obs
