import unittest

from lock import Lock

class LockTest(unittest.TestCase):
    
    def testDefaults(self):
        lock = Lock()
        self.assertEqual(lock._state, Lock.DEFAULT_STATE)
        self.assertEqual(lock._diameter, Lock.DEFAULT_DIAMETER)
        self.assertEqual(lock._needKey, False) # difference between lock._diameter and lock.diameter?

    def testSpecific(self):
        testDiameter : float = 1.15
        testState : bool  = True
        lock = Lock(state = testState, diameter = testDiameter)
        self.assertEqual(lock.diameter, testDiameter)
        self.assertEqual(lock.state, testState)
        self.assertEqual(lock._needKey, True)

    def testStateLocked(self): 
        testState : bool = True
        lock = Lock(state = testState, diameter = Lock.DEFAULT_DIAMETER)
        self.assertEqual(lock._needKey, True)

    def testStateUnlocked(self):
        testState : bool = False
        lock = Lock(state = testState, diameter = Lock.DEFAULT_DIAMETER)
        self.assertEqual(lock._needKey, False)


    if __name__ == '__main__':
        unittest.main()
        

       






    