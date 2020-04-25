import unittest
from door import Door

class DoorTest(unittest.TestCase):
    
    def testDefaults(self):
        door = Door()
        self.assertEqual(door.woodType, Door.DEFAULT_WOOD)
        self.assertEqual(door.height, Door.DEFAULT_HEIGHT)
        self.assertEqual(door.width, Door.DEFAULT_WIDTH)

    def testSpecific(self):
        testHeight : float = 85.8
        testWidth : float = 40
        testWood : str = 'Cedar' 
        door1 = Door(woodType = testWood, width = testWidth, height = testHeight)
        self.assertEqual(door1.woodType, testWood)
        self.assertEqual(door1.height, testHeight)
        self.assertEqual(door1.width, testWidth)
        