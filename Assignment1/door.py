from lock import Lock 
from handle import Handle

class Door:
    DEFAULT_WOOD : str = 'Mahogany'
    DEFAULT_HEIGHT : float = 80.2 # inches
    DEFAULT_WIDTH : float = 36.4 # inches

    def __init__(self, woodType : str = DEFAULT_WOOD, height : float = DEFAULT_HEIGHT, width : float = DEFAULT_WIDTH, lockdiameter : float = Lock.DEFAULT_DIAMETER, state : bool  = Lock.DEFAULT_STATE, handlediameter : float = Handle.DEFAULT_DIAMETER):
         self._woodType : str = woodType
         self._height : float = height
         self._width: float = width
         self._lock : Lock = Lock(lockdiameter)
         self._handle : Handle = Handle(handlediameter)

    @property
    def lock(self) -> Lock:
        return self._lock

    @property
    def handle(self) -> Handle:
        return self._handle
        
    @property
    def woodType(self) -> str:
        return self._woodType

    @property
    def height(self) -> float:
        return self._height
    
    @property
    def width(self) -> float:
        return self._width

    
