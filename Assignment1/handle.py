class Handle:
    DEFAULT_MATERIAL : str = 'Nickle'
    DEFAULT_FINISH : str = 'Brushed'
    DEFAULT_DIAMETER : float = 2.50 # inches

    def __init__(self, diameter : float = DEFAULT_DIAMETER, material : str = DEFAULT_MATERIAL, finish : str = DEFAULT_FINISH):
        self._diameter = diameter
        self._material = material
        self._finish = finish


    @property 
    def diameter(self) -> float:
        return self._diameter
    
    @property
    def material(self) -> str:
        return self._material

    @property
    def finish(self) -> str:
        return self._finish

    
    @material_and_finish.setter
    def material_and_finish(self, value: str) -> None:
        if value == 'Nickle':
            self._finish = 'Brushed'
        if value == 'Brass':
            self._finish = 'Matte'
        if value == 'Silver':
            self._finish = 'Polished'
        self._material = value