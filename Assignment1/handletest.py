import unittest

from handle import Handle

class HandleTest(unittest.TestCase):
    
    def testDefaults(self):
        handle = Handle()
        self.assertEqual(handle._material, Handle.DEFAULT_MATERIAL)
        self.assertEqual(handle._diameter, Handle.DEFAULT_DIAMETER)
        self.assertEqual(handle._finish, Handle.DEFAULT_FINISH) 

    def testSpecific(self):
        testDiameter : float = 2.75
        testMaterial : str  = 'Silver'
        handle = Handle(material = testMaterial, diameter = testDiameter)
        handle.finish = testMaterial
        self.assertEqual(handle.diameter, testDiameter)
        self.assertEqual(handle.material, testMaterial)
        self.assertEqual(handle.finish, 'Polished')


    if __name__ == '__main__':
        unittest.main()
        