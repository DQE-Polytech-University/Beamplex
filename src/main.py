from jsonloader import *
from refraction import *
from helmholtz import *

filePath = input('Enter path to .json file with laser structure in single brackets:')

log1 = Logger()
loader1 = JSONLoader(filePath, log1)

loader1.loadJSON()
loader1.parseJSONData()
