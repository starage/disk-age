#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:09:18 2024

@author: mac
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides the function Age(alpha) to calculate evolutionary age of a protoplanetary disk from its infrared (IR) SED slope alpha, according to the work of TBA. 

N.B.: You need to install scipy first.

Please use it in python by 
    from disk_age import *
    
Input: 
    alpha: float or array of float, the IR SED slope alpha; defaults to 0.0. It must be in the range: -2.0 ~ 4.8. Otherwise, the edge value of this range that is closest to the input value will be forced and a warning will be issued.

Output: 
    Age: float or a list of float, the corresponding disk ages (unit: Myr).
"""

from scipy.interpolate import splrep,splint
def Age(alpha=0.0):
    # the best observed histogram of IR SED slope alpha from that paer:
    histo_alpha = [-3.028380897,-2.946254679,-2.864128461,-2.782002244,-2.699876026,-2.617749808,-2.53562359,-2.453497372,-2.371371154,-2.289244937,-2.207118719,-2.124992501,-2.042866283,-1.960740065,-1.878613848,-1.79648763,-1.714361412,-1.632235194,-1.550108976,-1.467982758,-1.385856541,-1.303730323,-1.221604105,-1.139477887,-1.057351669,-0.975225452,-0.893099234,-0.810973016,-0.728846798,-0.64672058,-0.564594362,-0.482468145,-0.400341927,-0.318215709,-0.236089491,-0.153963273,-0.071837056,0.010289162,0.09241538,0.174541598,0.256667816,0.338794034,0.420920251,0.503046469,0.585172687,0.667298905,0.749425123,0.831551341,0.913677558,0.995803776,1.077929994,1.160056212,1.24218243,1.324308647,1.406434865,1.488561083,1.570687301,1.652813519,1.734939737,1.817065954,1.899192172,1.98131839,2.063444608,2.145570826,2.227697043,2.309823261,2.391949479,2.474075697,2.556201915,2.638328133,2.72045435,2.802580568,2.884706786,2.966833004,3.048959222,3.131085439,3.213211657,3.295337875,3.377464093,3.459590311,3.541716529,3.623842746,3.705968964,3.788095182,3.8702214,3.952347618,4.034473836,4.116600053,4.198726271,4.280852489,4.362978707,4.445104925,4.527231142,4.60935736,4.691483578,4.773609796]
    histo_value = [0.0023819208841714557,0.004763841768342911,0.015013319512353336,0.09763019162920789,0.02935552398513048,0.06458645281788387,0.07764814555100943,0.08474220392244569,0.06602909135115352,0.05514426617544548,0.08008511846801294,0.08691478722885525,0.05244655564442759,0.059163087165981905,0.04279173727390284,0.06660044101062922,0.1619540714985116,0.10237694779733657,0.12559551206554562,0.21627473716216472,0.43407476171946385,0.43707994711415815,0.5527457135264616,0.8848535756745809,0.9816534670846297,0.8654062918260428,0.7782584383003879,0.5837025233259185,0.539673764525941,0.549926598851997,0.34536452449736355,0.26546763844580323,0.25997170237429446,0.2128776933320493,0.16359565239662527,0.16766237010007534,0.1988306207718757,0.19033135601588805,0.19134871982190552,0.1413070166501613,0.1600019899025919,0.08486495798771844,0.1271351246409864,0.12284987670068093,0.1496631576128895,0.09602951870271567,0.13720405037983682,0.10796420140904284,0.1256788674807176,0.06593018837046792,0.06899429623782666,0.08256475877681028,0.07956032492322053,0.042291078366553124,0.05693919033111768,0.05946447720226208,0.0350872833770066,0.07008337466370014,0.08149385786040254,0.01887810784478204,0.02953423237372536,0.025009494028525085,0.018422316759415316,0.019445407100823323,0.0009514283137899997,0.036752862460113854,0.006796135785498052,0.004332074046476949,0.0029880516108251823,0.019268278793090423,0.0009832347835824085,0.0,0.0025431035003935978,0.0,0.0010439282887418052,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    # fit it with a smoothed cubic spline function:
    tck_36 = splrep(histo_alpha,histo_value,k=3,s=0.08) #This is the interpolation function on alpha histogram.
    alpha_max = 4.814672904812319 #The value is the max alpha in alpha histogram.
    
    # evaluate the disk age(s):
    if type(alpha) in [int, float]:
        if alpha<-2: print(f'\n\033[31mWarning! Too small input alpha value ({alpha}) is forced to the allowed lower limit of -2.\033[0m\n')
        elif alpha>4.8: print(f'\n\033[31mWarning! Too large input alpha value ({alpha}) is forced to the allowed upper limit of 4.8.\033[0m\n')
        alpha=min(max(alpha,-2),4.8)
        Age = splint(alpha_max,alpha,tck_36)*2/splint(-0.3,-1.6,tck_36) #
    else:
        Age = []
        for i in alpha:
            if i<-2: print(f'\n\033[31mWarning! Too small input alpha value ({i}) is forced to the allowed lower limit of -2.\033[0m\n')
            elif i>4.8: print(f'\n\033[31mWarning! Too large input alpha value ({i}) is forced to the allowed upper limit of 4.8.\033[0m\n')
            a=min(max(i,-2),4.8)
            Age.append( splint(alpha_max,a,tck_36)*2/splint(-0.3,-1.6,tck_36) )
    return Age


# Input the data of Fig.3 and Fig.5
data_array_fig = []
with open('data_fig.txt') as f:
    for line1 in f:
        data_list = line1.split()
        data_array = [float(i) for i in data_list]
        data_array_fig.append(data_array)
# Create a new dictionary to store data of Fig.3 and Fig.5
dict_fig = {}
# Add data to dictionary
# Fig.3
dict_fig["alpha_fig3"] = data_array_fig[0] # X axis value of alpha in Fig.3
dict_fig["a_average_fig3"] = data_array_fig[1] # The average of paramneter a in each alpha bin
dict_fig["a_average_error_fig3"] = data_array_fig[2] # The error of average of paramneter a in each alpha bin
dict_fig["a_std_fig3"] = data_array_fig[3] # The standard deviation of paramneter a in each alpha bin

dict_fig["alpha_model_fig3"] = data_array_fig[4] # for 200710 models
dict_fig["a_average_model_fig3"] = data_array_fig[5]
dict_fig["a_average_error_model_fig3"] = data_array_fig[6]
dict_fig["a_std_model_fig3"] = data_array_fig[7]

# Fig.5 (first and second columns)
dict_fig["alpha_L_fig5"] = data_array_fig[8] # X axis value of alpha in Fig.5 (the X-coordinate grid of all the panels in the left two columns is the same)

dict_fig["L3.6_average_fig5"] = data_array_fig[9] # The average of 3.6um luminosity in each alpha bin
dict_fig["L3.6_std_fig5"] = data_array_fig[10] # The standard deviation of 3.6um luminosity in each alpha bin
dict_fig["L3.6_average_error_fig5"] = data_array_fig[11] # The error of average of 3.6um luminosity in each alpha bin

dict_fig["L4.5_average_fig5"] = data_array_fig[12] # 4.5um
dict_fig["L4.5_std_fig5"] = data_array_fig[13]
dict_fig["L4.5_average_error_fig5"] = data_array_fig[14]

dict_fig["L5.8_average_fig5"] = data_array_fig[15] # 5.8um
dict_fig["L5.8_std_fig5"] = data_array_fig[16]
dict_fig["L5.8_average_error_fig5"] = data_array_fig[17]

dict_fig["L8_average_fig5"] = data_array_fig[18] #8um
dict_fig["L8_std_fig5"] = data_array_fig[19]
dict_fig["L8_average_error_fig5"] = data_array_fig[20]

dict_fig["L24_average_fig5"] = data_array_fig[21] #24um
dict_fig["L24_std_fig5"] = data_array_fig[22]
dict_fig["L24_average_error_fig5"] = data_array_fig[23]

dict_fig["L3.6_average_model_fig5"] = data_array_fig[24] #for 200710 models
dict_fig["L3.6_std_model_fig5"] = data_array_fig[25]
dict_fig["L3.6_average_error_model_fig5"] = data_array_fig[26]

dict_fig["L4.5_average_model_fig5"] = data_array_fig[27]
dict_fig["L4.5_std_model_fig5"] = data_array_fig[28]
dict_fig["L4.5_average_error_model_fig5"] = data_array_fig[29]

dict_fig["L5.8_average_model_fig5"] = data_array_fig[30]
dict_fig["L5.8_std_model_fig5"] = data_array_fig[31]
dict_fig["L5.8_average_error_model_fig5"] = data_array_fig[32]

dict_fig["L8_average_model_fig5"] = data_array_fig[33]
dict_fig["L8_std_model_fig5"] = data_array_fig[34]
dict_fig["L8_average_error_model_fig5"] = data_array_fig[35]

dict_fig["L24_average_model_fig5"] = data_array_fig[36]
dict_fig["L24_std_model_fig5"] = data_array_fig[37]
dict_fig["L24_average_error_model_fig5"] = data_array_fig[38]

# Fig.5 (third and fourth columns)
dict_fig["L_a_fig5"] = data_array_fig[39] # Y axis value of luminosity in Fig.5 (the Y-coordinate grid of all the panels in the right two columns is the same)

dict_fig["a_vs_L3.6_average_fig5"] = data_array_fig[40] # The average of parameter 'a' in each 3.6 um luminosity bin
dict_fig["a_vs_L3.6_average_error_fig5"] = data_array_fig[41] # The error of average of parameter 'a' in each 3.6 um luminosity bin
dict_fig["a_vs_L3.6_std_fig5"] = data_array_fig[42] # The standard deviation of parameter 'a' in each 3.6 um luminosity bin

dict_fig["a_vs_L4.5_average_fig5"] = data_array_fig[43] # 4.5um
dict_fig["a_vs_L4.5_average_error_fig5"] = data_array_fig[44]
dict_fig["a_vs_L4.5_std_fig5"] = data_array_fig[45]

dict_fig["a_vs_L5.8_average_fig5"] = data_array_fig[46] # 5.8um
dict_fig["a_vs_L5.8_average_error_fig5"] = data_array_fig[47]
dict_fig["a_vs_L5.8_std_fig5"] = data_array_fig[48]

dict_fig["a_vs_L8_average_fig5"] = data_array_fig[49] # 8um
dict_fig["a_vs_L8_average_error_fig5"] = data_array_fig[50]
dict_fig["a_vs_L8_std_fig5"] = data_array_fig[51]

dict_fig["a_vs_L24_average_fig5"] = data_array_fig[52] # 24um
dict_fig["a_vs_L24_average_error_fig5"] = data_array_fig[53]
dict_fig["a_vs_L24_std_fig5"] = data_array_fig[54]

dict_fig["a_vs_L3.6_average_model_fig5"] = data_array_fig[55] # for 200710 models
dict_fig["a_vs_L3.6_average_error_model_fig5"] = data_array_fig[56]
dict_fig["a_vs_L3.6_std_model_fig5"] = data_array_fig[57]

dict_fig["a_vs_L4.5_average_model_fig5"] = data_array_fig[58]
dict_fig["a_vs_L4.5_average_error_model_fig5"] = data_array_fig[59]
dict_fig["a_vs_L4.5_std_model_fig5"] = data_array_fig[60]

dict_fig["a_vs_L5.8_average_model_fig5"] = data_array_fig[61]
dict_fig["a_vs_L5.8_average_error_model_fig5"] = data_array_fig[62]
dict_fig["a_vs_L5.8_std_model_fig5"] = data_array_fig[63]

dict_fig["a_vs_L8_average_model_fig5"] = data_array_fig[64]
dict_fig["a_vs_L8_average_error_model_fig5"] = data_array_fig[65]
dict_fig["a_vs_L8_std_model_fig5"] = data_array_fig[66]

dict_fig["a_vs_L24_average_model_fig5"] = data_array_fig[67]
dict_fig["a_vs_L24_average_error_model_fig5"] = data_array_fig[68]
dict_fig["a_vs_L24_std_model_fig5"] = data_array_fig[69]
