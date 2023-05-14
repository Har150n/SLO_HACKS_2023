class Game:
    MINIMUM_CORRECT = 20
    def __init__(self, score, level,progress_bar, level_index=0, q_index=0):
        self.score = score             #int -> number of correct answers for the level
        self.level = level          #List[Level] -> List of Level Objects
        self.level_index = level_index #int -> current level number
        self.q_index = q_index         #int -> total questions asked
        self.progress_bar = progress_bar #int -> percentage progress to display


    def populateLevels(self):
        #DUMMY DATA
        # level_1_images = {"happy.jpg": "happy", "sad.jpg": "sad"}
        # level_1 = Level(1, level_1_images)
        # self.levels = [level_1]

        #get DeepFace processing data
        # image_dict = {}
        # for level in self.levels:
        #     #add level classifying later
        #     level.images = image_dic
        pass

    #checks the answer against the correct emotion
    def checkAnswer(self, imageName, answer):
        level = self.level[self.level_index]
        self.q_index += 1
        if level.images[imageName] == answer:
            self.score += 1
            #self.ans_streak += 1 (if time)

            #update progress bar
            if self.q_index <= 20:
                self.progress_bar = self.score/20
            else:
                self.progress_bar = self.score/self.q_index

            # check level up: minimum questions reached and at least 80% progress bar
            if self.q_index >= 20 and self.score/self.q_index >= 0.8:
                self.level_index += 1
                self.restart()

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


