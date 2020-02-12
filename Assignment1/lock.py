class Lock:
    DEFAULT_STATE : bool = False # is the lock locked(true) or unlocked(false)
    DEFAULT_DIAMETER : float = 2.16 # inches

    def __init__(self, diameter : float = DEFAULT_DIAMETER, state : bool = DEFAULT_STATE):
        self._diameter = diameter
        self._state = state

    @property 
    def diameter(self) -> float:
        return self._diameter
    
    @property
    def state(self) -> bool:
        return self._state

    
    @state.setter
    def state(self, value: bool) -> None:
        