from src.Game import Game
from dotenv import load_dotenv
from pygame import init, quit

if __name__ == "__main__":
    load_dotenv(dotenv_path="settings")
    init()
    Game().run()
    quit()