import json
import os
import sys

class Logger:
    def pressAnyKey( self, exitMessage ):
        print(exitMessage)
        os.system('pause')
        sys.exit()

class JSONLoader:
    
    def __init__(self, filename, L1 = Logger()):
        self.fileName = filename
        self.jsonLogger = L1
        
    def loadJSON( self ):
        try:
            with open(self.fileName) as jsonFile:
                self.jsonData = json.load(jsonFile)
        except IOError:
            self.jsonLogger.pressAnyKey(self.fileName + ": file not found")
        except ValueError:
            self.jsonLogger.pressAnyKey(self.fileName + ": syntax error")
        finally:
            print(self.fileName + " successfully loaded")

    def parseJSONData(self):
        try:
            self.jsonConcentration = []
            self.jsonThickness = []
            self.jsonWavelength = self.jsonData["wavelength"]
            self.jsonLayersNumber = self.jsonData["layersNumber"]
            for i in range(self.jsonLayersNumber):
                self.jsonConcentration.append( self.jsonData["layers"][i]["concentration"])
                self.jsonThickness.append( self.jsonData["layers"][i]["thickness"])
        except KeyError:
            self.jsonLogger.pressAnyKey(".json: data not found")
        except IndexError:
            self.jsonLogger.pressAnyKey(".json: actual number of layers does not match with layersNumber value")

        if isinstance( self.jsonWavelength, (int, float)) == False or isinstance( self.jsonLayersNumber, (int, float)) == False or isinstance( self.jsonThickness, (list)) == False or isinstance( self.jsonConcentration, (list)) == False:
            self.jsonLogger.pressAnyKey(".json: type mismatch")
        for i in range( self.jsonLayersNumber):
            if isinstance(self.jsonConcentration[i], (int, float)) == False or isinstance( self.jsonThickness[i], (int, float)) == False:
                self.jsonLogger.pressAnyKey(".json: type mismatch")
            if self.jsonConcentration[i] <= 0 or self.jsonConcentration[i] >= 1 or self.jsonThickness <= 0:
                self.jsonLogger.pressAnyKey(".json: data out of range")

        if self.jsonWavelength < 0.85 or self.jsonWavelength > 1.5 or self.jsonLayersNumber <= 0:
            self.jsonLogger.pressAnyKey(".json: data out of range")

        print(".json file successfully parsed")
        return(( self.jsonWavelength, self.jsonLayersNumber, self.jsonConcentration, self.jsonThickness))


