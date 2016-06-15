import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.refraction import *

class TestRefractionOutput(unittest.TestCase):

    def setUp(self):
        self.calc = RefractionCalc(0.85, [0.45, 0.35, 0.02, 0.35, 0.45])

    def testAlGaAs(self):
        self.assertTrue(self.calc.refraction_AlGaAs(self.calc.concentration[0]) == 3.331564442988186)

    def testInGaAs(self):
        self.assertTrue(self.calc.refraction_InGaAs(self.calc.concentration[2]) == 3.6962077867407275)

    def testComputeRefraction(self):
        self.calc.computeRefraction()
        out = [3.331564442988186, 3.393487851264978, 3.6962077867407275, 3.393487851264978, 3.331564442988186]
        self.assertTrue(self.calc.refraction == out)

if __name__ == '__main__':
    unittest.main()
