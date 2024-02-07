Usage: This module provides the function Age(alpha) to calculate the evolutionary age of a protoplanetary disk from its infrared (IR) SED slope alpha, according to the work of TBA. 

You can click the 'code' button above to download the ZIP file. Then, you can unzip it and use help('disk_age') in Python in the same working directory of the unzipped files to get more information.

An example:
  from disk_age import Age
  import numpy as np
  help('disk_age')
  alpha_array = np.linspace(-2,4,500)
  Age_array = Age(alpha_array)
