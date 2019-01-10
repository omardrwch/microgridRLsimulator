import numpy as np
from  microgridRLsimulator.gym_wrapper import MicrogridEnv


# Initialize environment
env = MicrogridEnv()

# Compute cumulative reward of a random policy
sum_reward = 0
T = 2  # horizon
for tt in range(T):
    action = env.action_space.sample()
    next_state, reward, done, info = env.step(action)
    sum_reward += reward

