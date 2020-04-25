import unittest

from lock import Lock

class LockTest(unittest.TestCase):
    
    def testDefaults(self):
        lock = Lock()
        self.assertEqual(lock._state, Lock.DEFAULT_STATE)
        self.assertEqual(lock._diameter, Lock.DEFAULT_DIAMETER)

    def testSpecific(self):
        testDiameter1 : float = 1.15
        testState : bool  = True
        lock = Lock(state = testState, diameter = testDiameter1)
        self.assertEqual(lock.diameter, testDiameter1)
        self.assertEqual(lock.state, testState)
        

    def testStateLocked(self): 
        testState1 : bool = True
        lock1 = Lock(state = testState1)
        lock1.set_needKey = testState1
        self.assertEqual(lock1._state, True)
        self.assertEqual(lock1._needKey, True)
       
  

    def testStateUnlocked(self):
        testState2 : bool = False
        lock2= Lock(state = testState2)
        lock2.set_needKey = testState2
        self.assertEqual(lock2._state, False) #It isn't being called here either
        self.assertEqual(lock2._needKey, False)


    if __name__ == '__main__':
        unittest.main()
        

       






    