import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import random

class Bot:

    def __init__(self):
        self.auto_names = [""]

    def run(self, game_pin, nickname):

        #set selenium options
        opts = Options()

        #set to be headless
        opts.set_headless()
        assert opts.headless

        #make a browser instance
        browser = Firefox(options=opts)

        #load kahoot page
        browser.get("https://kahoot.it")

        #find pin input and submit pin
        input_form = browser.find_element_by_id('game-input')
        input_form.send_keys(game_pin)
        input_form.submit()

        #wait, so that the page is loaded
        browser.implicitly_wait(10)

        #find nickname input and submit nickname
        nickname_form = browser.find_element_by_id("nickname")
        nickname_form.send_keys(nickname)
        nickname_form.submit()

        browser.implicitly_wait(10)

        #wait for game to start, then click random button. repeat
        while True:
            while True:
                print(browser.current_url)
                try:
                    #if browser.current_url == "https://kahoot.it/v2/ranking" or browser.current_url == "https://kahoot.it/v2/answer/result":
                    #    browser.close()
                    buttons = browser.find_elements_by_tag_name("button")
                    if len(buttons) < 4:
                        continue
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    #if browser.current_url == "https://kahoot.it/v2/ranking" or browser.current_url == "https://kahoot.it/v2/answer/result":
                    #    browser.close()
                    continue

            answer = random.choice(buttons)
            time.sleep(random.choice([0.75, 1, 2]))
            answer.click()

    def auto(self, num):
        pass
