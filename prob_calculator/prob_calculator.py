import copy
import numpy as np
import random
from collections import Counter
# Consider using the modules imported above.

class Hat():

    def __init__(self, **kwargs):
        self.contents = [*Counter(kwargs).elements()]
    
    def draw(self, balls_to_draw: int) -> list:
        
        if balls_to_draw >= len(self.contents):
            contents_copy = copy.deepcopy(self.contents)
            self.contents = []
            
            return contents_copy
        
        else:
            chosen_balls = []

            for i in range(balls_to_draw):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                chosen_balls.append(ball)

            return chosen_balls

  
def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    
    num_ocurrencies = 0

    for i in range(num_experiments):

        hat_copy = copy.deepcopy(hat)

        chosen_balls = hat_copy.draw(num_balls_drawn)
        chosen_balls_dict = dict(Counter(chosen_balls))

        matches = 0

        for k, v in expected_balls.items():

            try:
                if v <= chosen_balls_dict[k]:
                    matches += 1
            except:
                pass
        
        if matches == len(expected_balls):
            num_ocurrencies += 1

    return np.round(num_ocurrencies / num_experiments, 3)
