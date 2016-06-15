import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.refraction import *

class TestRefractionInput(unittest.TestCase):

    def testInputCorrect(self):
        try:
            self.calc = RefractionCalc(0.85, [0.1, 0.1, 0.1, 0.1, 0.1])
        except Exception, error:
            self.fail(error)
    
    def testInitLambda(self):
        self.assertRaises(TypeError, RefractionCalc, '0.85', [0.1, 0.1, 0.1, 0.1, 0.1])
        self.assertRaises(TypeError, RefractionCalc, None, [0.1, 0.1, 0.1, 0.1, 0.1])
        self.assertRaises(ValueError, RefractionCalc, 0.5, [0.1, 0.1, 0.1, 0.1, 0.1])
        self.assertRaises(ValueError, RefractionCalc, 2, [0.1, 0.1, 0.1, 0.1, 0.1])

    def testInitConcentration(self):
        self.assertRaises(TypeError, RefractionCalc, 0.85, '[1]')
        self.assertRaises(TypeError, RefractionCalc, 0.85, None)
        self.assertRaises(TypeError, RefractionCalc, 0.85, [0.1, 0.2, '0.3', 0.1, 0.1])
        self.assertRaises(ValueError, RefractionCalc, 0.85, [-0.1, 0.2, 0.3, 0.1, 0.1])
        self.assertRaises(ValueError, RefractionCalc, 0.85, [0.1, 1.2, 0.3, 0.1, 0.1])

    def testAlGaAs(self):
        self.calc = RefractionCalc(0.85, [0.1, 0.1, 0.1, 0.1, 0.1])
        with self.assertRaises(TypeError):
            self.calc.refraction_AlGaAs('5')
        with self.assertRaises(TypeError):
            self.calc.refraction_AlGaAs(None)
        with self.assertRaises(ValueError):
            self.calc.refraction_AlGaAs(-1)
        with self.assertRaises(ValueError):
            self.calc.refraction_AlGaAs(2)

    def testInGaAs(self):
        self.calc = RefractionCalc(0.85, [0.1, 0.1, 0.1, 0.1, 0.1])
        print(self.calc.wavelength)
        with self.assertRaises(TypeError):
            self.calc.refraction_InGaAs('5')
        with self.assertRaises(TypeError):
            self.calc.refraction_InGaAs(None)
        with self.assertRaises(ValueError):
            self.calc.refraction_InGaAs(-1)
        with self.assertRaises(ValueError):
            self.calc.refraction_InGaAs(2)
        

if __name__ == '__main__':
    unittest.main()
