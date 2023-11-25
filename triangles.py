#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

import turtle

def triangle(t, len):
    if len > 10:
        for i in range(3):
            t.forward(len)
            t.left(120)
        triangle(t, len/2)

def nestedTriangle(t, len):
    if len > 10:
        for i in range(3):
            t.forward(len)
            t.left(120)
            nestedTriangle(t, len/2)
