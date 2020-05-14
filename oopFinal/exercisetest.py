import unittest

from exercise import Exercise

class ExerciseTest(unittest.TestCase):
    

    def testDefaults(self):
        exercise_test = Exercise("Box Jumps", False, "Legs")
        self.assertEqual(exercise_test.reps, Exercise.DEFAULT_REPS)
        self.assertEqual(exercise_test.weight, Exercise.DEFAULT_WEIGHT)

    def testSpecifics(self):
        test_name : str = "Pull Ups"
        test_aerobic : bool = False
        test_category : str = "Arms"
        test_reps : int = 30
        test_weight : int = 10

        exercise1_test = Exercise(name = test_name, aerobic = test_aerobic, category = test_category, reps = test_reps, weight = test_weight)
        self.assertEqual(exercise1_test.name, test_name)
        self.assertEqual(exercise1_test.aerobic, test_aerobic)
        self.assertEqual(exercise1_test.category, test_category)
        self.assertEqual(exercise1_test.reps, test_reps)
        self.assertEqual(exercise1_test.weight, test_weight)
        

