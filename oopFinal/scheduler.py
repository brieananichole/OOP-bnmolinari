import random
from exercise import Exercise
from categories import Legs, Arms, Cardio, Back, Abs

muscle_group = ['Legs', 'Arms' , "Cardio", "Back", 'Abs', "Rest" , "Rest"]

class Day:

    def __init__(self, name : str):
        self._name = name
        self._category = random.choice(muscle_group)
        muscle_group.remove(self._category) #no repetitions in the week

    @property
    def name(self) -> str:
        return self._name

    @property
    def category(self) -> str:
        return self._category
    

class Week(Day):

    def __init__(self, ):
        self.week = [] #empty list to represent the weekly schedule
        self.week.append(Day('Sunday'))
        self.week.append(Day('Monday'))
        self.week.append(Day('Tuesday'))
        self.week.append(Day('Wednesday'))
        self.week.append(Day('Thursday'))
        self.week.append(Day('Friday'))
        self.week.append(Day('Saturday'))
    





workout_Brie = Week()