from exercise import Exercise

#Each targeted muscle group has a class which is a child class to the parent class Exercise

class Legs(Exercise):
    num_of_leg_exercises = 0
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps = 20
    raise_weight = 10 #lbs

    def __init__(self, name, aerobic, category, reps : int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

        Legs.num_of_leg_exercises += 1
    
    @property 
    def reps(self) -> str:
        return '{} reps'.format(self._reps)

    @property
    def weight(self) -> str:
        return '{} lbs'.format(self._weight)

    @reps.setter
    def reps(self, value : int) -> None:
        self._reps = value

    @weight.setter
    def weight(self, value : int) -> None:
        self._weight = value

    def setDifficulty(self, value : str):
        if value == 'Intermediate':
            self._reps += self.raise_reps
            self._weight += self.raise_weight
        elif value == 'Hard':
            self._reps += (2 * self.raise_reps)
            self._weight += (2 * self.raise_weight)
        else: 
            pass
    

class Arms(Exercise):
    num_of_arm_exercises = 0
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps : int = 10 
    raise_weight : int  = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

        Arms.num_of_arm_exercises += 1

    
    @property 
    def reps(self) -> str:
        return '{} reps'.format(self._reps)

    @property
    def weight(self) -> str:
        return '{} lbs'.format(self._weight)

    @reps.setter
    def reps(self, value : int) -> None:
        self._reps = value

    @weight.setter
    def weight(self, value : int) -> None:
        self._weight = value

    def setDifficulty(self, value : str):
        if value == 'Intermediate':
            self._reps += self.raise_reps
            self._weight += self.raise_weight
        elif value == 'Hard':
            self._reps += (2 * self.raise_reps)
            self._weight += (2 * self.raise_weight)
        else: 
            pass
   


class Abs(Exercise):
    num_of_ab_exercises = 0
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps = 15
    raise_weight = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

        Abs.num_of_ab_exercises += 1

    
    @property 
    def reps(self) -> str:
        return '{} reps'.format(self._reps)

    @property
    def weight(self) -> str:
        return '{} lbs'.format(self._weight)

    @reps.setter
    def reps(self, value : int) -> None:
        self._reps = value

    @weight.setter
    def weight(self, value : int) -> None:
        self._weight = value

    def setDifficulty(self, value : str):
        if value == 'Intermediate':
            self._reps += self.raise_reps
            self._weight += self.raise_weight
        elif value == 'Hard':
            self._reps += (2 * self.raise_reps)
            self._weight += (2 * self.raise_weight)
        else: 
            pass

    
    
class Back(Exercise):
    num_of_back_exercises = 0
    DEFAULT_REPS : int = 10
    DEFAULT_WEIGHT : int = 0
    raise_reps = 5
    raise_weight = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

        Back.num_of_back_exercises += 1

    
    @property 
    def reps(self) -> str:
        return '{} reps'.format(self._reps)

    @property
    def weight(self) -> str:
        return '{} lbs'.format(self._weight)

    @reps.setter
    def reps(self, value : int) -> None:
        self._reps = value

    @weight.setter
    def weight(self, value : int) -> None:
        self._weight = value

    def setDifficulty(self, value : str):
        if value == 'Intermediate':
            self._reps += self.raise_reps
            self._weight += self.raise_weight
        elif value == 'Hard':
            self._reps += (2 * self.raise_reps)
            self._weight += (2 * self.raise_weight)
        else: 
            pass


class Cardio(Exercise):
    num_of_cardio_exercises = 0
    DEFAULT_INTERVAL : int = 30 #seconds
    raise_interval : int = 15 #seconds

    def __init__(self, name, aerobic, category, interval : int = DEFAULT_INTERVAL):
        super().__init__(name, aerobic, category)
        self._interval = interval

        Cardio.num_of_cardio_exercises += 1

    @property
    def interval(self) -> str:
        return '{} seconds'.format(self._interval)

    @interval.setter
    def intervalSetter(self, value : int) -> None:
        self._interval = value

    def setDifficulty(self, value : str):
        if value == 'Intermediate':
            self._interval += self.raise_interval
        elif value == 'Hard':
            self._interval += (2 * self.raise_interval)
        else: 
            pass



#testing code

##abs_1 = Abs('Crunches', False, 'Abs')
##print(isinstance(abs_1, Exercise))
##print(abs_1.reps)

##abs_1.setDifficulty('Intermediate')
##print(abs_1.weight)

##print(Exercise.num_of_exercises)
##print(Arms.num_of_arm_exercises)
##print(Abs.num_of_ab_exercises)