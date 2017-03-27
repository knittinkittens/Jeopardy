#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:13:23 2017

"""

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        
    def getPoints(self):
        return self.points
    
    def addPoints(self, val):
        self.points += val
        
    def subtractPoints(self, val):
        self.points -= val