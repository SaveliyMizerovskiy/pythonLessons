#CSci 127 Teaching Staff
#October 2017
#A program that summarizes images, like koalastothemax
#Modified by: Saveliy Mizerovskiy
#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import numpy as np
import matplotlib.pyplot as plt


def average(region):
    img1 = np.array(region)
    return (np.average(img1[:,:,0]),np.average(img1[:,:,1]),np.average(img1[:,:,2]))

def setRegion(region, r,g,b):
    region[:,:,0] = r
    region[:,:,1] = g
    region[:,:,2] = b