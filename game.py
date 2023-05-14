import upload
import functions
import pandas as pd
class Game:

    score = 0               #number of correct answers for the level
    levels = []             #List[Level] -> List of Level Objects
    level_index = 0
    q_index = 0
    progress_bar = 0
    populated = False

def populateLevels():
    emotions = upload.prompt_upload()   #dictionary of (image, emotion)
    i = 1
    for emotion in emotions:
        print("Image: " + str(i) + "    " + emotion + "         " + emotions[emotion])
        i+= 1
    levelOne = Level(1,emotions)
    Game.levels.append(levelOne)

#checks the answer against the correct emotion
def checkAnswer(answer, root_home, windows):
    level = Game.levels[Game.level_index]
    if level.images[Game.q_index][1] == answer:
        Game.score += 1
        Game.q_index += 1
        # check level up: minimum questions reached and at least 80% progress bar
        if Game.q_index >= 20 and Game.score/Game.q_index >= 0.8:
            Game.level_index += 1
            restart()
    functions.create_game_window(root_home, windows)
    root_home.destroy()


def restart():
    Game.score = 0
    Game.q_index = 0




class Level:
    def __init__(self, level_num, images):
        self.level_num = level_num      #int -> current level number
        self.images =list(images.items())       #dict ->  key: image name, value: list of emotions
        self.count = len(self.images)


