import json
import os
import sys

#loads .json file, describing laser structure, and extracts data from it
class JSONLoader:
    
    def __init__(self, filename):
        if isinstance(filename, str) == False:
            raise TypeError("wrong path")
        self.fileName = filename

    #loads .json file 
    def loadJSON( self ):
        try:
            with open(self.fileName) as jsonFile:
                self.data = json.load(jsonFile)
        except IOError:
            raise IOError(": file not found")
        except ValueError:
            raise ValueError(": syntax error")
        print(self.fileName + " successfully loaded")

    #parses .json file and returns laser structure parameters
    def parseJSONData(self):      
        try:
            self.concentration = []
            self.thickness = []
            self.wavelength = self.data["wavelength"]
            for i in range(5):
                self.concentration.append( self.data["layers"][i]["concentration"])
                self.thickness.append( self.data["layers"][i]["thickness"])
        except KeyError:
            raise KeyError(".json: data not found")
        except IndexError:
            raise IndexError(".json: actual number of layers does not match with layersNumber value")

        if isinstance( self.wavelength, (int, float)) == False or isinstance( self.thickness, (list)) == False or isinstance( self.concentration, (list)) == False:
            raise TypeError(".json: type mismatch")
        for i in range(5):
            if isinstance(self.concentration[i], (int, float)) == False or isinstance( self.thickness[i], (int, float)) == False:
                raise TypeError(".json: type mismatch")
            if self.concentration[i] <= 0 or self.concentration[i] >= 1 or self.thickness[i] <= 0:
                raise ValueError(".json: data out of range")

        if self.wavelength < 0.85 or self.wavelength > 1.5:
            raise ValueError(".json: data out of range")
        
        if self.concentration is None:
            raise ValueError("self.concentration is undefined")
        if self.thickness is None:
            raise ValueError("self.thickness is undefined")
        if self.wavelength is None:
            raise ValueError("self.wavelength is undefined")

        print(".json file successfully parsed")
        return(( self.wavelength, self.concentration, self.thickness))
       
