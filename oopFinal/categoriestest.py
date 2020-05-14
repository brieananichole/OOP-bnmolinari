import unittest
from exercise import Exercise
from categories import Legs, Back, Arms, Cardio, Abs

class LegsTest(unittest.TestCase):
    
    def testDefaults(self):
        legs_1 = Legs("Deadlifts", False, "Legs")
        self.assertEqual(isinstance(legs_1, Exercise), True)
        self.assertEqual(legs_1.reps, Legs.DEFAULT_REPS)
        self.assertEqual(legs_1.weight, Legs.DEFAULT_WEIGHT)

    def testSpecifics(self):
        test_name : str = "Jump Squats"
        test_aerobic : bool = False
        test_category : str = "Legs"
        test_reps : int = 40
        test_weight : int = 30

        legs_2 = Legs(name = test_name, aerobic = test_aerobic, category = test_category, reps = test_reps, weight = test_weight)

        self.assertEqual(legs_2.name, test_name)
        self.assertEqual(legs_2.aerobic, test_aerobic)
        self.assertEqual(legs_2.category, test_category)
        self.assertEqual(legs_2.reps, test_reps)
        self.assertEqual(legs_2.weight, test_weight)

    def testSetDifficulty(self):
        legs_3 = Legs("Sumo Deadlifts", False, "Legs")

        legs_3.setDifficulty('Intermediate')
        self.assertEqual(legs_3.reps, 40)
        self.assertEqual(legs_3.weight, 10)

        legs_4 = Legs("Good Mornings", False, "Legs")

        legs_4.setDifficulty('Hard')
        self.assertEqual(legs_4.reps, 60)
        self.assertEqual(legs_4.weight, 20)
        



class ArmsTest(unittest.TestCase):
    pass

class AbsTest(unittest.TestCase):
    pass

class CardioTest(unittest.TestCase):
    pass

class BackTest(unittest.TestCase):
    pass

