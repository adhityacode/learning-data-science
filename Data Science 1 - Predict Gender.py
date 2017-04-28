# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:48:15 2017

@author: Reza
"""

'''
from sklearn import tree

X = [
    [181,80,44],
    [177,70,43],
    [160,60,38],
    [154, 54, 37],
    [166, 65, 40],
    [190, 90, 47],
    [175, 64, 39],
    [177, 70, 40],
    [159, 55, 37],
    [171, 75, 42],
    [181, 85, 43]
]

print X
Y = ['male', 'female', 'female', 'female', 'male' ,'male', 'male', 'female', 'male', 'female', 'male' ]
'''

X = [[0, 0], [1, 1]]
Y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[2., 2.], [0.1, 0.1]])
print prediction