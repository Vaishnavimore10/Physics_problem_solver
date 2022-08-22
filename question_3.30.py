import math
import random , copy
import numpy as np
from sympy import *
def generate(data):

    # Generate random data for problem variant:
    t = random.choice([2.5,3.6,4.2,5])
    length = random.choice([3,5,4,7])
    vertical = random.choice([6,7,3,5])
    hori = random.choice([4,2,3,5])






    # Analysis:           (DIMENSIONS OF THE FIGURE SHOULD BE KEPT CONSTANT)
    Ai= (76-vertical)*(25-hori) + (38-vertical)*25
    tou = t* 10**6/(2 * 4 *Ai)
    ds= (25-hori)/vertical + 38/hori +(25/vertical) + (38-vertical)/hori + (50-hori)/vertical + (76- vertical)/hori
    angle = ((t * length)/4* Ai*Ai*79) * ds
    angle_ans = math.degrees(angle)


    # Return randomized parameters and results to HTML file:
    data['params']['t'] = t
    data['params']['length'] = length
    data['params']['vertical'] = vertical
    data['params']['hori']= hori
    data['correct_answers']['tou'] = tou
    data['correct_answers']['angle_ans']=angle_ans

