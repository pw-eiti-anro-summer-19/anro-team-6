#!/usr/bin/env python

from numpy import *
import math

#length of link
a1 = 0
a2 = 0.03
a3 = 0,01 

#Angles
theta_1 = 0
theta_2 = 0
theta_3 = 0

theta_1 = (theta_1/180)*pi
theta_2 = (theta_2/180)*pi
theta_3 = (theta_3/180)*pi

#DH parameter
#theta, d, ai-1, arfa
M = np.array([[theta_1, 0, a1, 0],
              [theta_2, 0, a2, 0],
              [theta_3, 0, a3, pi/2]])

m_1 = np.array([[cos(M[0][1]), -sin(M[0][1]), 0, M[0][2],
                [(sin(M[0][1]) * cos(M[0][4])), cos(M[0][1]) * cos(M[0][4]], -sin(M[0][4]), 0],
                [(sin(M[0][1]) * sin(M[0][4])), cos(M[0][1]) * sin(M[0][4]], cos(M[0][4]), 0],
                [0, 0, 0, 1]])

m_2 = np.array([[cos(M[1][1]), -sin(M[1][1]), 0, M[1][2],
                [(sin(M[1][1]) * cos(M[1][4])), cos(M[1][1]) * cos(M[1][4]], -sin(M[1][4]), 0],
                [(sin(M[1][1]) * sin(M[1][4])), cos(M[1][1]) * sin(M[1][4]], cos(M[1][4]), 0],
                [0, 0, 0, 1]])

m_3 = np.array([[cos(M[2][1]), -sin(M[2][1]), 0, M[2][2],
                [(sin(M[2][1]) * cos(M[2][4])), cos(M[2][1]) * cos(M[2][4]], -sin(M[2][4]), 0],
                [(sin(M[2][1]) * sin(M[2][4])), cos(M[2][1]) * sin(M[2][4]], cos(M[2][4]), 0],
                [0, 0, 0, 1]])

M = np.matmul(m_1, m_2, m_3)
