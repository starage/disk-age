Usage: This module provides the function "Age(α)" to calculate the evolutionary age of a protoplanetary disk from its infrared (IR) SED slope, α, as showed in Fig.A1 of the paper [Liu et al. 2024RAA....24g5001L](https://ui.adsabs.harvard.edu/abs/2024RAA....24g5001L/abstract). It also provides the data of the new relationships among the luminosity, α and SED concavity in Fig.2 and Fig.B1 of the same paper.

You can click the 'code' button above to download the ZIP file. Then, unzip it and use help('disk_age') in Python in the same working directory of the unzipped files to get more information.

An example of usage:  
  from disk_age import *  
  import numpy as np  
  help('disk_age')  
  alpha_array = np.linspace(-2,4.8,100)  
  Age_list = Age(alpha_array)  

The data for Fig.2 and Fig.B1 is stored in the dictionary 'dict_fig'.

Please cite our following papers if your research has benefitted from these data curves:
First discovery of the α-disk age conversion relation:

[Liu et al. 2023ApJ...943...39L](https://ui.adsabs.harvard.edu/abs/2023ApJ...943...39L/abstract)

An update to the α-disk age conversion relation and the luminosity, α, SED concavity correlations:

[Liu et al. 2024RAA....24g5001L](https://ui.adsabs.harvard.edu/abs/2024RAA....24g5001L/abstract)
