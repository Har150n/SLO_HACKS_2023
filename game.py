class Game:
    def __init__(self, score, levels, level_index=0):
        self.score = score             #int -> score of the current run
        self.levels = levels           #List[Level] -> List of Level Objects
        self.level_index = level_index #int -> current level number


    def restart(self):
        self.score = 0
        self.level_index = 0



class Level:
    def __init__(self, level_num, images):
        self.level_num = level_num      #int -> current level number
        self.images = images            #dict ->  key: image name, value: list of emotions


