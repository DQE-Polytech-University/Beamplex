import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.laserstructure import *

class TestLaserstructureInput(unittest.TestCase):

    def testInitCorrect(self):
        try:
            self.laser = Laser((0.85, [0.1, 0.1, 0.1, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        except Exception, error:
            self.fail(error)
    
    def testInitLambda(self):
        self.assertRaises(TypeError, Laser, ('0.85', [0.1, 0.1, 0.1, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        self.assertRaises(TypeError, Laser, (None, [0.1, 0.1, 0.1, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        self.assertRaises(ValueError, Laser, (0.5, [0.1, 0.1, 0.1, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        self.assertRaises(ValueError, Laser, (2, [0.1, 0.1, 0.1, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))

    def testInitConcentration(self):
        self.assertRaises(TypeError, Laser, (0.85, '[1]', [0.5, 0.5, 0.5, 0.5, 0.5]))
        self.assertRaises(TypeError, Laser, (0.85, None, [0.5, 0.5, 0.5, 0.5, 0.5]))
        self.assertRaises(TypeError, Laser, (0.85, [0.1, 0.2, '0.3', 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        #self.assertRaises(ValueError, Laser, (0.85, [-0.1, 0.2, 0.3, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))
        #self.assertRaises(ValueError, Laser, (0.85, [0.1, 1.2, 0.3, 0.1, 0.1], [0.5, 0.5, 0.5, 0.5, 0.5]))

    def testInitThickness(self):
        self.assertRaises(TypeError, Laser, (0.85, [0.5, 0.5, 0.5, 0.5, 0.5], '[1]'))
        self.assertRaises(TypeError, Laser, (0.85, [0.5, 0.5, 0.5, 0.5, 0.5], None,))
        self.assertRaises(TypeError, Laser, (0.85, [0.5, 0.5, 0.5, 0.5, 0.5], [0.1, 0.2, '0.3', 0.1, 0.1]))
        #self.assertRaises(ValueError, Laser, (0.85, [0.5, 0.5, 0.5, 0.5, 0.5], [-0.1, 0.2, 0.3, 0.1, 0.1]))

if __name__ == '__main__':
    unittest.main()
