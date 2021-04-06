import kahoot

def main(game_pin, nickname):

    bot = kahoot.Bot()

    bot.run(game_pin, nickname)

if __name__ == "__main__":
    game_pin = input("Please provide the game pin: ")
    nickname = input("Please provide the bot's nickname: ")
    main(game_pin, nickname)
