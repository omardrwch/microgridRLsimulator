import gym
from microgridRLsimulator.gym_wrapper import MicrogridEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

import matplotlib.pyplot as plt
import numpy as np

# env = gym.make('CartPole-v1')
env = MicrogridEnv()
env_dummy = DummyVecEnv([lambda: env])  # The algorithms require a vectorized environment to run

model = PPO2(MlpPolicy, env_dummy, verbose=1)
model.learn(total_timesteps=80000)


obs = env.reset()

T = 23*50
rewards_vec = []
for i in range(T):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    rewards_vec.append(rewards)
    if done:
        obs = env.reset()
    # env.render()


env.simulator.store_and_plot()

plt.hist(rewards_vec)
plt.show()