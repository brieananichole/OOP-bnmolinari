class Exercise:
    
    num_of_exercises = 0
    DEFAULT_REPS : int = 10
    DEFAULT_WEIGHT : int = 0

    def __init__(self, name : str, aerobic : bool, category : str, reps : int = DEFAULT_REPS, weight : int = DEFAULT_WEIGHT):
        self._name = name
        self._aerobic = aerobic
        self._category = category
        self._reps = reps
        self._weight = weight

        Exercise.num_of_exercises += 1 #increments number of exercises within class each time new instance is created

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def aerobic(self) -> bool:
        return self._aerobic
    
    @property
    def category(self) -> str:
        return self._category
        
    @property 
    def reps(self) -> str:
        return '{} reps'.format(self._reps)

    @property
    def weight(self) -> str:
        return '{} lbs'.format(self._weight)


    @name.setter
    def name(self, value : str) -> None:
        self.name = value

    @aerobic.setter
    def aerobic(self, value : bool) -> None:
        self.aerobic = value

    @category.setter
    def category(self, value : str) -> None:
        self.category = value

    @reps.setter
    def reps(self, value : int) -> None:
        self.reps = value

    @weight.setter
    def weight(self, value : int) -> None:
        self.weight = value



