class Game:
    MINIMUM_CORRECT = 20
    def __init__(self, score, levels, level_index=0):
        self.score = score             #int -> number of correct answers for the level
        self.levels = levels           #List[Level] -> List of Level Objects
        self.level_index = level_index #int -> current level number


    def populateLevels(self):
        #DUMMY DATA
        level_1_images = {"happy.jpg": "happy", "sad.jpg": "sad"}
        level_1 = Level(1, level_1_images)
        self.levels = [level_1]

        #get DeepFace processing data
        # image_dict = {}
        # for level in self.levels:
        #     #add level classifying later
        #     level.images = image_dict

    #checks the answer against the correct emotion
    def checkAnswer(self, imageName, answer):
        level = self.levels[self.level_index]
        if level[imageName] == answer:
            self.score += 1
            self.checkScore()
            return True
        else:
            return False


    def restart(self):
        self.score = 0
        self.level_index = 0



class Level:
    def __init__(self, level_num, images, qIndex):
        self.level_num = level_num      #int -> current level number
        self.images = images            #dict ->  key: image name, value: list of emotions
        self.qIndex = qIndex


