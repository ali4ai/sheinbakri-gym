import gym
import gym_sheinbakri  # Ensure this matches your module name

env = gym.make("SheinBakri-v0")

obs = env.reset()  # Initialize environment
done = False

while not done:
    env.render()  # Visualize game state
    action = env.action_space.sample()  # Select a random action
    obs, reward, done, info = env.step(action)
    print(f"Action: {action}, Reward: {reward}, Done: {done}")

env.close()  # Close Pygame window