import random, os, time

WORDS = ["APPLE", "HAPPY", "PLANT", "GRAPE", "WATER", "CHAIR", "QUEEN", "TABLE", "OCEAN", "HOUSE", "SMILE", "EARTH", "DREAM", "BREAD", "DANCE", "ROUND", "CLICK", "TIGER", "RIVER", "CLOUD", "ANGEL", "MOUSE", "LEMON", "BEACH", "CREAM", "HORSE", "SPACE", "TRAIN", "SNAKE", "HONEY", "MUSIC", "BRUSH", "FRUIT", "CHESS", "BRAIN", "CLOWN", "GHOST", "CAMEL", "SHELL", "HAPPY", "BREAD", "LUNCH", "WATCH", "CLOCK", "PLANT", "CHAIR", "TIGER", "CREAM", "EAGLE", "WATER", "SMOKE", "PIANO", "LIGHT", "WINDY", "PILOT", "PUNCH", "THUMB", "PLATE", "GRASS", "FLOOR", "GLOVE", "JELLY", "CRAFT", "KNEEL", "BLINK", "CHALK", "PRIDE", "TRUTH", "VIBES", "WAVES", "DELTA", "BERRY", "FIERY", "IVORY", "ROCKY", "STORM", "ZEBRA", "SILKY", "FLAME", "TREND", "QUICK", "GLORY", "LEAFY", "ZESTY", "SLICE", "SWEET", "CRISP", "DARKS", "QUIET", "DRIVE", "GLASS"]
word = None

COLORS = {
    "GREEN": "\033[32m", # correct
    "YELLOW": "\033[33m", # correct but index of
    "GRAY": "\033[36m", # letter not found
    "RED": "\033[31m",
}

tries = []


def coloredWords() -> str:
    colored_words = ""

    for j, tried_word in enumerate(tries):        
        colored_words += "  "

        for i, letter in enumerate(tried_word):
            if word[i] == letter:
                colored_words += COLORS["GREEN"] + letter
            elif letter in word:
                colored_words += COLORS["YELLOW"] + letter
            else:
                colored_words += COLORS["GRAY"] + letter
        
        if j + 1 != len(tries):
            colored_words += "\n"

    return colored_words


def generateWord():
    return random.choice(WORDS)


while True:
    os.system("clear")

    if word == None:
        word = generateWord()
    else:
        print(coloredWords())

        word_in = input("➜ ").upper()

        if len(word_in) != 5:
            continue
        else:
            tries.append(word_in)

        if tries[-1] == word:
            print(COLORS["RED"] + "WON THE GAME")
            time.sleep(3)
            word = generateWord()
            tries = []
