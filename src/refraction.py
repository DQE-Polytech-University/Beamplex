#Planck constant in eV and speed of light in vacuum in micrometers
h = 4.1356 * 10 ** (-15)
cl = 2.998 * 10 ** 14

#computes refraction profile for the given laser structure
class RefractionCalc:
    concentration = []
    refraction = []
    wavelength = 0
    
    def __init__(self, lyambda, concentration):
        
        if isinstance(lyambda, (int, float)) == False:
            raise TypeError("lyambda should be a number")
        if isinstance(concentration, list) == False:
            raise TypeError("concentration should be a list")
        for i in range(5):
            if isinstance(concentration[i], (int, float)) == False:
                raise TypeError("concentration elements should be numbers")
                break
            
        if lyambda is None:
            raise ValueError("lyambda is undefined")
        if concentration is None:
            raise ValueError("concentration is undefined")
            
        if lyambda < 0.85 or lyambda > 1.5:
            raise ValueError("lyambda out of range")
        for i in range(5): 
            if concentration[i] <= 0 or concentration[i] >= 1:
                raise ValueError("concentration out of range")
            
        
        self.concentration = concentration
        self.wavelength = lyambda
        
    #index of refraction Al_x Ga_1-x As calculation    
    def refraction_AlGaAs(self, concentration):	
        
        if isinstance(self.wavelength, (int, float)) == False:
            raise TypeError("self.wavelength should be a number")
        if isinstance(concentration, (int, float)) == False:
            raise TypeError("self.concentration should be a number")
        if self.wavelength is None:
            raise ValueError("self.wavelength is undefined")
        if self.concentration is None:
            raise ValueError("self.concentration is undefined")
        if self.wavelength < 0.8 or self.wavelength > 1.5:
            raise ValueError("self.wavelength out of range")
        if concentration <= 0 or concentration >= 1:
            raise ValueError("concentration out of range")
            
        A0 = 6.3 + 19 * concentration
        B0 = 9.4 - 10.2 * concentration
        E0 = 1.425 + 1.155 * concentration + 0.37 * concentration ** 2
        delta0 = 0.34 - 0.04 * concentration
        chi = h * cl / (self.wavelength * E0)
        chiSO = h * cl / (self.wavelength * (E0 + delta0))
        fSO =  (2 - (1 + chiSO) ** 0.5 - (1 - chiSO) ** 0.5)/ chiSO ** 2
        f = (2 - (1 + chi) ** 0.5 -(1 - chi) ** 0.5)/ chi ** 2
        n = (A0 * (f + fSO/2 * (E0 / (E0 + delta0)) ** 1.5) + B0) ** 0.5
        return n
    
    #index of refraction In_x Ga_1-x As calculation
    def refraction_InGaAs(self, concentration):	
        
        if isinstance(self.wavelength, (int, float)) == False:
            raise TypeError("self.wavelength should be a number")
        if isinstance(concentration, (int, float)) == False:
            raise TypeError("self.concentration should be a number")
        if self.wavelength is None:
            raise ValueError("self.wavelength is undefined")
        if self.concentration is None:
            raise ValueError("self.concentration is undefined")
        if self.wavelength < 0.8 or self.wavelength > 1.5:
            raise ValueError("self.wavelength out of range")
        if concentration <= 0 or concentration >= 1:
            raise ValueError("concentration out of range")
        
        A = 8.95
        B = 2.054
        C = 0.6245
        Eggaas = 1.424
        E00 = 1.424 - 1.56 * concentration + 0.494 * concentration ** 2
        n = (A + B/ (1 - (C * Eggaas / (self.wavelength * E00)) ** 2)) ** 0.5
        return n

    #computes an array of refractive indicies for all layers
    def computeRefraction(self):
        
        if isinstance(self.concentration, list) == False:
            raise TypeError("concentration should be a list")
        for i in range(5):
            if isinstance(self.concentration[i], (int, float)) == False:
                raise TypeError("concentration elements should be numbers")
                break
        if self.concentration is None:
            raise ValueError("concentration is undefined")
        for i in range(5): 
            if self.concentration[i] <= 0 or self.concentration[i] >= 1:
                raise ValueError("concentration out of range")
                
        self.refraction = [0 for i in range(5)]
        for i in [0, 1, 3, 4]:
            self.refraction[i] = self.refraction_AlGaAs(self.concentration[i])
        self.refraction[2] = self.refraction_InGaAs(self.concentration[2])
