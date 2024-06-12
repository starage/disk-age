Usage: This module provides the function Age(alpha) to calculate the evolutionary age of a protoplanetary disk from its infrared (IR) SED slope alpha as showed in Fig.A1. It also provides the data of the new relationships among the luminosity, IR SED slope and SED concavity in Fig.2 and Fig.B1 in the work of TBA.

You can click the 'code' button above to download the ZIP file. Then, you can unzip it and use help('disk_age') in Python in the same working directory of the unzipped files to get more information.

An example:  
  from disk_age import *  
  import numpy as np  
  help('disk_age')  
  alpha_array = np.linspace(-2,4.8,100)  
  Age_list = Age(alpha_array)  

The data for Fig.2 and Fig.B1 is stored in the dictionary 'dict_fig'.
