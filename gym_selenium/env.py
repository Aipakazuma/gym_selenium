from .envs.game import KnockknockJP


import gym
import numpy as np


class MyEnv(gym.Env):
    def __init__(self, game_url=None):
        super().__init__()
        self.env = KnockknockJP(game_url=game_url)
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Box(
            low=0,
            high=1,
            shape=(5,)
        )
        self.reward_range = [-1, 1]

    def reset(self):
        self.env.reset()
        action = np.random.randint(0,
                                   self.action_space.n)
        observation, _, _, _ = self.step(action)
        return observation

    def step(self, action):
        _action = self.env.enable_actions[action]
        observation, reward, done, info = \
            self.env.step(_action)

        return observation, reward, done, info

    def render(self, mode='human', close=False):
        outfile = None
        return outfile

    def close(self):
        pass

    def seed(self, seed=None):
        return super().seed(seed)
