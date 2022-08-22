import math
import random , copy
import numpy as np
from sympy import *
def generate(data):

    # Generate random data for problem variant:
    power = random.choice([2.4,3.6,1.8,4.2])
    RPM = random.choice([18,22,38,30])
    set1 = [1/2,1/3,1/6]
    set2 = [1/7,3/7,3/7]
    set3 = [1/5,2/5,4/10]
    attri = random.choice([set1,set2,set3])
    shear = random.choice([150,200,250,320])
    L_ma = random.choice([3,4,2,5])
    L_ab = random.choice([2,3,4,1])
    L_bc = random.choice([2,3,4,1])





    # Analysis:

    Tm = (power*6600)/(RPM*(math.pi/30))
    Ta = Tm*attri[0]
    Tb = Tm*attri[1]
    Tc = Tm*attri[2]
    T_ma=Tm
    T_ab = Tm-Ta
    T_bc = Tm-Ta-Tb
    T_max= (1/3)*shear
    θ = 11.5 * (10**6)
    θ_mc = 4.4

    # consider T limit
    diameter_t = ((16*T_max)/(math.pi*T_max))**(1/3)

    # consider θ limit
    diameter_θ = ((32/math.pi*θ*θ_mc*(math.pi/180))*(T_ma*L_ma + T_ab*L_ab +T_bc*L_bc))**(1/4)

    # maximum diameter
    diameter_max = max(diameter_t,diameter_θ)



    # Return randomized parameters and results to HTML file:
    data['params']['power'] = power
    data['params']['RPM'] = RPM
    data['params']['shear'] = shear
    data['params']['l1'] = attri[0]
    data['params']['l2'] = attri[1]
    data['params']['l3'] = attri[2]
    data['correct_answers']['diameter_max'] = diameter_max


