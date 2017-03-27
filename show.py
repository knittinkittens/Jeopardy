#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:11:53 2017

"""

class Show(object):
    
    def __init__(self, show, qs, level = 1):
        self.show       = show 
        self.categories = qs[(qs.show == self.show) & (qs.q_type == level)].categories.unique()
        self.level      = level
        self.finished   = 0

    def getShow(self):
        return self.show
    
    def setCategories(self, level, qs):
        self.categories = qs[(qs.show == self.show) & (qs.q_type == level)].categories.unique()
        
    def getCategories(self):   
        return self.categories
    
    def completeShow(self, complete):
        self.finished = 1
        
    def getFinished(self):
        return self.finished
         