# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:48:12 2017

@author: Reza
"""

import numpy as np
from ligthfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))