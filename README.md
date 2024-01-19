Usage: This module provides the function Age(alpha) to calculate evolutionary age of a protoplanetary disk from its infrared (IR) SED slope alpha, according to the work of Liu et al. (2024). 
       After downloading the module, use help('disk_age') to get more information.

An example:
  from disk_age import Age
  help('disk_age')
  alpha_array = np.linspace(-2,4,500)
  Age_array = Age(alpha_test_2024)
