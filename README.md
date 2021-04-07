# kahoot-bot

Python script to connect to kahoot autonomously (using Selenium) and answer questions randomly. No, the bot cannot get correct answers as kahoot do not show what button represents what answer, so this is physically impossible.

`Note:` This is not intended for spam; hence you can only connect 1 bot unless you run the program multiple times.

## Usage

Run `main.py`. This will prompt two inputs, one for the game pin and one for the nickname. Game pin must be an integer and nickname must be less than or equal to 15 characters long.

`Note:` At the moment the bot cannot detect if your nickname was taken. This will be fixed soon.

The bot will only answer 'quiz' type questions; puzzles and other types it will ignore.

*Last updated 07/03/2021*
