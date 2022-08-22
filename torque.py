import math
import random , copy
import numpy as np
from sympy import *
def generate(data):

    # Generate random data for problem variant:
    T = random.choice([4, 8, 16,13])
    thickness = random.choice([1.25, 2.25, 3.05, 4.8])
    tubelength = 75        #the dimensions of the hollow tube are kept constant
    tubethickness= 5

    x = tubelength-thickness
    Ai = x*x/1000
    tou = t*1000/(2*tubethickness*Ai)


    # Analysis:
    x = tubelength-thickness
    Ai = x*x/1000
    tou= t*1000/(2*tubethickness*Ai)
    angle = (t*thickness*(t*x/tubethickness))/4*Ai*Ai*79*10**9
    angle_degree=math.degrees(angle)


    # Return randomized parameters and results to HTML file:
    data['params']['T'] = T
    data['params']['thickness'] = thickness
    data['correct_answers']['tou'] = tou
    data['correct_answers']['angle_degree'] = angle_degree
