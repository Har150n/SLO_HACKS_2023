import upload

class Game:

    score = 0               #number of correct answers for the level
    levels = []             #List[Level] -> List of Level Objects
    level_index = 0
    q_index = 0
    progress_bar = 0

def populateLevels():
    emotions = upload.prompt_upload()   #dictionary of (image, emotion)
    levelOne = Level(1,emotions, 0)
    Game.levels.append(levelOne)

#checks the answer against the correct emotion
def checkAnswer(imageName, answer, levels, level_index):
    level = levels[level_index]
    Game.q_index += 1
    if level.images[imageName] == answer:
        Game.score += 1

        #update progress bar
        if Game.q_index <= 20:
            Game.progress_bar = Game.score/20
        else:
            Game.progress_bar = Game.score/Game.q_index

        # check level up: minimum questions reached and at least 80% progress bar
        if Game.q_index >= 20 and Game.score/Game.q_index >= 0.8:
            Game.level_index += 1
            restart()

        return True
    else:
        return False


def restart():
    Game.score = 0
    Game.q_index = 0



class Level:
    def __init__(self, level_num, images, qIndex):
        self.level_num = level_num      #int -> current level number
        self.images = images            #dict ->  key: image name, value: list of emotions
        self.qIndex = qIndex


