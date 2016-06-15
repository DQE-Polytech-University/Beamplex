import unittest
import sys
from os import *
import os
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class TestLaserstructureOutput(unittest.TestCase):
    mainPath = path.dirname(path.dirname(path.abspath(__file__))) + '\src\main.py'
    jsonPath = os.path.join(path.dirname(path.dirname(path.abspath(__file__))), 'tests\json_test_files\correct.json')

    def testMain(self):
        try:
            os.system('python ' + self.mainPath + ' ' + self.jsonPath + ' 999')
        except Exception, error:
            self.fail(error)
        
if __name__ == '__main__':
    unittest.main()
