from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import numpy as np


GAME_URL = 'http://knockknock.jp/sample/MatterJS/index.html'


class KnockknockJP():
    """誰かが作ったjavascriptゲーム.
    """

    def __init__(self, game_url=None, headless=None):
        self.name = 'knockknock_jp'
        # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
        options = Options()
        options.add_argument('--no-sandbox')
        if headless:
            # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
            options.add_argument('--headless')

        # ChromeのWebDriverオブジェクトを作成する。
        self.driver = Chrome(chrome_options=options)

        # Googleのトップ画面を開く。
        self.driver.get(GAME_URL if game_url is None else game_url)
        self.enable_actions = [None, Keys.SPACE]

    def reset(self):
        self.game_start()
        return None, None

    def step(self, action):
        if action is not None:
            self.driver.find_element_by_tag_name('body').send_keys(action)

        states = self.driver.get_screenshot_as_png()
        game_over = self.game_over()
        reward = 0
        reward += 0.1
        if game_over:
            reward -= 1

        return states, reward, game_over, {}

    def game_start(self):
        self.driver.find_element_by_tag_name('body') \
            .send_keys(self.enable_actions[1])

    def game_over(self):
        _id = self.driver.find_element_by_id('js-panelOutro')
        return _id.is_displayed()


def main(episode=10, game_url=None):
    game = KnockknockJP()

    # gameの進行
    try:
        for e in range(episode):
            _, reward = game.reset()
            print('start episode: {}'.format(e))
            rewards = 0
            # action
            while True:
                action = np.random.choice(game.enable_actions)
                states, reward, done, _ = game.step(action)
                rewards += reward

                if done:
                    print('end episode: {}, reward: {}'.format(
                        e, rewards, reward, done))
                    break

    except KeyboardInterrupt:
        # ブラウザーを終了する。
        game.driver.quit()


if __name__ == '__main__':
    game_url = None
    main(game_url=game_url)
