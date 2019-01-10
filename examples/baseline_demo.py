import gym
from  microgridRLsimulator.gym_wrapper import MicrogridEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

import matplotlib.pyplot as plt
import numpy as np

# env = gym.make('CartPole-v1')
env = MicrogridEnv()
env = DummyVecEnv([lambda: env])  # The algorithms require a vectorized environment to run

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=80000)

obs = env.reset()

T = int(1e5)
rewards_vec = np.zeros(T)
for i in range(T):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    rewards_vec[i] = rewards
    # env.render()

plt.hist(rewards_vec)
plt.show()