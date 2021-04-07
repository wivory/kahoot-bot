import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import random
import sys
import logging

"""
Bot class for connecting to kahoot.
"""

class Bot:
    """
    Bot class to connect to kahoot.
    run() will:
        Make a selenium headless browser instance
        Input pin and nickname
        Loop checking for buttons to press
        Pick a random answer button and press
        Check for game end
        If the game is ended then will exit
    """

    def __init__(self):
        pass

    def run(self, game_pin, nickname):
        """Run the bot. Connects the bot to the game pin specified, with the nickname specified."""

        #set selenium options to headless mode, then connect to browser instance
        opts = Options()
        opts.set_headless()
        assert opts.headless
        self.browser = Firefox(options=opts)

        #join the game with pin and nickname
        self.join_game(game_pin, nickname)

        logging.info(f"Connected bot with name '{nickname}' to game with pin {game_pin}")

        #wait for page to load
        self.browser.implicitly_wait(10)

        #wait for game to start, then click random button. repeat
        while True:
            while True:
                try:
                    self.check_end()
                    buttons = self.browser.find_elements_by_tag_name("button")
                    if len(buttons) < 4:
                        continue
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    self.check_end()
                    continue
            logging.info("Answering question with random answer")
            self.random_answer(buttons)

    def join_game(self, pin, nick):
        """Join game specified"""
        self.browser.get("https://kahoot.it")
        self.input_pin(pin)
        #wait for page to load
        self.browser.implicitly_wait(10)
        self.input_nick(nick)

    def input_pin(self, pin):
        """Find pin input and submit"""
        input_form = self.browser.find_element_by_id('game-input')
        input_form.send_keys(pin)
        input_form.submit()

    def input_nick(self, nick):
        """Find nickname input and submit"""
        nickname_form = self.browser.find_element_by_id("nickname")
        nickname_form.send_keys(nick)
        nickname_form.submit()

    def random_answer(self, buttons):
        """Pick a random answer from the answer buttons, wait for a random time (for human feel) then click"""
        answer = random.choice(buttons)
        time.sleep(random.choice([0.75, 1, 2]))
        answer.click()

    def check_end(self):
        """Exits the program if the game has ended."""
        if self.browser.current_url == "https://kahoot.it/v2/ranking":
            self.browser.close()
            logging.info("Game ended, exiting...")
            sys.exit()
