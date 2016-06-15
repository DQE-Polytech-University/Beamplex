import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.laserstructure import *

class TestLaserstructureOutput(unittest.TestCase):

    def setUp(self):
        self.laser = Laser((0.85, [0.8, 0.8, 0.8, 0.8, 0.8], [0.8, 0.8, 0.8, 0.8, 0.8]))
        self.laser.gridX = [x for x in range(25)]
        self.laser.gridN = [x ** 2 for x in range(25)]
        self.laser.field = [x ** 3 for x in range(25)]

    def testPlotRefraction(self):
        try:
            self.laser.plotRefraction()
        except Exception, error:
            self.fail(error)

    def testPlotField(self):  
        try:
            self.laser.plotField()
        except Exception, error:
            self.fail(error)

if __name__ == '__main__':
    unittest.main()
