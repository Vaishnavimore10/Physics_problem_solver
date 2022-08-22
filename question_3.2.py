import math
import random , copy
import numpy as np
from sympy import *
def generate(data):

    # Generate random data for problem variant:
    angle = random.choice([2.4,3.6,1.8,4.2])
    d = random.choice([18,22,38,30])
    l = random.choice([1.5,2.2,3.2,4])




    # Analysis:
    stress = (d * math.radians(angle))/2*l*1000


    # Return randomized parameters and results to HTML file:
    data['params']['angle'] = angle
    data['params']['d'] = d
    data['params']['l'] = l
    data['correct_answers']['stress'] = stress

