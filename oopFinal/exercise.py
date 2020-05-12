class Exercise:
    
    num_of_exercises = 0

    def __init__(self, name : str, aerobic : bool, category : str):
        self._name = name
        self._aerobic = aerobic
        self._category = category

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

    @name.setter
    def name(self, value : str) -> None:
        self.name = value

    @aerobic.setter
    def aerobic(self, value : bool) -> None:
        self.aerobic = value

    @category.setter
    def category(self, value : str) -> None:
        self.category = value


