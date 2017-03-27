#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:12:26 2017

"""

from show import Show

class Category(Show):
    
    def __init__(self, Show, name, qs):
        self.show       = Show.getShow()
        self.name       = name
        self.questions  = list(qs[(qs.show == self.show) & (qs.categories == name) & (qs.completed == 0)].index.unique())
        self.values     = list(qs[(qs.show == self.show) & (qs.categories == name) & (qs.completed == 0)].clue_value.unique())
        self.completed  = 0

    def getCategory(self):
        return self.name
    
    def getQuestionIndexes(self):
        return self.questions
    
    def getValues(self):
        return self.values
    
    def completed(self, complete):
        self.completed = 1
    
    def getCompleted(self):
        return self.completed
    
    def getNumberLeft(self, qs):
        return len(qs[(qs.show == self.show) & (qs.categories == self.name) & (qs.completed == 0)])
    
    def setQuestions(self, qs):
        self.questions = list(qs[(qs.show == self.show) & (qs.categories == self.name) & (qs.completed == 0)].index.unique())
        
    def setValues(self, qs):
        self.values = list(qs[(qs.show == self.show) & (qs.categories == self.name) & (qs.completed == 0)].clue_value.unique())