import json
import os
import sys


class JSONLoader:
    
    def __init__(self, filename):
        if isinstance(filename, str) == False:
            raise TypeError("wrong path")
        self.fileName = filename
     

    def loadJSON( self ):
        try:
            with open(self.fileName) as jsonFile:
                self.jsonData = json.load(jsonFile)
        except IOError:
            raise IOError(": file not found")
        except ValueError:
            raise ValueError(": syntax error")
        print(self.fileName + " successfully loaded")


    def parseJSONData(self):
        

        try:
            self.jsonConcentration = []
            self.jsonThickness = []
            self.jsonWavelength = self.jsonData["wavelength"]
            for i in range(5):
                self.jsonConcentration.append( self.jsonData["layers"][i]["concentration"])
                self.jsonThickness.append( self.jsonData["layers"][i]["thickness"])
        except KeyError:
            raise KeyError(".json: data not found")
        except IndexError:
            raise IndexError(".json: actual number of layers does not match with layersNumber value")

        if isinstance( self.jsonWavelength, (int, float)) == False or isinstance( self.jsonThickness, (list)) == False or isinstance( self.jsonConcentration, (list)) == False:
            raise TypeError(".json: type mismatch")
        for i in range(5):
            if isinstance(self.jsonConcentration[i], (int, float)) == False or isinstance( self.jsonThickness[i], (int, float)) == False:
                raise TypeError(".json: type mismatch")
            if self.jsonConcentration[i] <= 0 or self.jsonConcentration[i] >= 1 or self.jsonThickness[i] <= 0:
                raise ValueError(".json: data out of range")

        if self.jsonWavelength < 0.85 or self.jsonWavelength > 1.5:
            raise ValueError(".json: data out of range")
        
        if self.jsonConcentration is None:
            raise ValueError("self.jsonConcentration is undefined")
        if self.jsonThickness is None:
            raise ValueError("self.jsonThickness is undefined")
        if self.jsonWavelength is None:
            raise ValueError("self.jsonWavelength is undefined")

        print(".json file successfully parsed")
        return(( self.jsonWavelength, self.jsonConcentration, self.jsonThickness))



        
