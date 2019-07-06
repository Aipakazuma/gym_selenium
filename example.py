from gym_selenium.env import MyEnv

import numpy as np


def main(env, episode=10):
    # gameの進行
    try:
        for e in range(episode):
            _, reward = env.reset()
            print('start episode: {}'.format(e))
            rewards = 0
            # action
            while True:
                action = np.random.choice(env.enable_actions)
                states, reward, done, _ = env.step(action)
                rewards += reward

                if done:
                    t = 'end episode: {}, reward: {}'
                    print(t.format(e, rewards,
                                   reward, done))
                    break

    except KeyboardInterrupt:
        # ブラウザーを終了する。
        env.driver.quit()


if __name__ == '__main__':
    env = MyEnv()
    np.random.seed(123)
    env.seed(123)
    nb_actions = env.action_space.n
    main(env)
