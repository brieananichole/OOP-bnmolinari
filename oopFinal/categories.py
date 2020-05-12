from exercise import Exercise

#Each targeted muscle group has a class which is a child class to the parent class Exercise

class Legs(Exercise):
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps = 20
    raise_weight = 10 #lbs

    def __init__(self, name, aerobic, category, reps : int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight
    
    @property 
    def reps(self) -> int:
        return self._reps

    @property
    def weight(self) -> int:
        return self._weight

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
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps : int = 10 
    raise_weight : int  = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

    
    @property 
    def reps(self) -> int:
        return self._reps

    @property
    def weight(self) -> int:
        return self._weight

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
    DEFAULT_REPS : int = 20
    DEFAULT_WEIGHT : int = 0
    raise_reps = 15
    raise_weight = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

    
    @property 
    def reps(self) -> int:
        return self._reps

    @property
    def weight(self) -> int:
        return self._weight

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
    DEFAULT_REPS : int = 10
    DEFAULT_WEIGHT : int = 0
    raise_reps = 5
    raise_weight = 5 #lbs

    def __init__(self, name, aerobic, category, reps: int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        super().__init__(name, aerobic, category)
        self._reps = reps
        self._weight = weight

    
    @property 
    def reps(self) -> int:
        return self._reps

    @property
    def weight(self) -> int:
        return self._weight

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
    DEFAULT_INTERVAL : int = 30 #seconds
    raise_interval : int = 15 #seconds

    def __init__(self, name, aerobic, category, interval : int = DEFAULT_INTERVAL):
        super().__init__(name, aerobic, category)
        self._interval = interval

    @property
    def interval(self) -> int:
        return self._interval

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
