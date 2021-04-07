import kahoot
import sys
import logging

"""
File to get input, then make a Bot instance and run.
"""

def main(game_pin, nickname):
    """Make an instance and run"""
    bot = kahoot.Bot()
    try:
        bot.run(game_pin, nickname)
    except ValueError:
        print("Your game pin was not valid.")
        sys.exit()

def get_input():
    """Get game pin and nickname"""
    pin = input("Input game pin: ")
    try:
        pin = int(pin)
    except ValueError:
        print("Game pin must be an integer.")
        sys.exit()
    nick = input("Input nickname: ")
    return pin, nick

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    pin, nick = get_input()
    main(pin, nick)
