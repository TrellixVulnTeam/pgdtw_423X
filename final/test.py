#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:39:46 2018

@author: paolograniero
"""
import libdtw as lib
import numpy as np

ref = np.array([1,3,5,3,3,3,4,7,5,6]).reshape(-1,1)
query = np.array([1,1.5,2,1,3,4,2]).reshape(-1,1)

d = lib.dtw()

distMatrix = d.CompDistMatrix(ref, query, "euclidean", 1)

print(distMatrix)

acc = d.CompAccDistmatrix(distMatrix, "symmetricP2")

print(acc)

warp = d.GetWarpingPath(acc, "symmetricP2")
print(warp)
