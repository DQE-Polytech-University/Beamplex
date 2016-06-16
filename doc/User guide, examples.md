##User guide, examples 
To specify a semiconductor structure it needs to fill a text file `laserstructure.json`. It's necessary to specify the following parameters:
Wavelength [0.8 - 1.5 µm], the thickness [>0] and concentration [0 - 1 (not including bounds)] for each of the five layers.

For download of the programm uoy need to set in the command line  the name of the load module – `python main.py laserstructure.json 999.` 
***(999-total number of points.)




##Examples
__1.INPUT DATA__

    {                                
     "wavelength": 0.930,
     "layersNumber": 5,                     
    "layers": [                           
    {                                     
      "thickness": 1,
      "concentration": 0.82
    },    
    {                                     
      "thickness": 1.2,
      "concentration": 0.83
    },    
    {                                     
      "thickness": 0.01,
      "concentration": 0.84
    },    
    {                                     
      "thickness": 1.4,
      "concentration": 0.85
    },    
    {                                     
      "thickness": 1.8,
      "concentration": 0.86
    }                            
    ]                                                     
    }   
__OUTPUT DATA__
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/field.png)



![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/refraction.png)

__2.INPUT DATA__

    {                                         
    "wavelength": 1,                    
    "layers": [                           
    {                                     
      "thickness": 1,
      "concentration": 0.6
    },    
    {                                     
      "thickness": 0.6,
      "concentration": 0.4
    },    
    {                                     
      "thickness": 0.01,
      "concentration": 0.05
    },    
    {                                     
      "thickness": 0.6,
      "concentration": 0.4
    },    
    {                                     
      "thickness": 1,
      "concentration": 0.6
    }                            
    ]                                                     
    } 

__OUTPUT DATA__
![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/field%20(2).png)



![1](https://raw.githubusercontent.com/DQE-Polytech-University/Beamplex/master/doc/refraction%20(2).png)