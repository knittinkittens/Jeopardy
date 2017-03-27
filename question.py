#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:12:55 2017

"""

from category import Category

class Question(Category):
    
    def __init__(self, Category, value, qs):
        self.category   = Category.getCategory()
        self.q_value    = value
        self.q_text     = qs[(qs.index.isin(Category.getQuestionIndexes())) & (qs.categories == self.category) & (qs.clue_value == value)].question.unique()
        self.q_answer   = qs[(qs.index.isin(Category.getQuestionIndexes())) & (qs.categories == self.category) & (qs.clue_value == value)].answer.unique()
        
    def getCategory(self):
        return self.category
    
    def getValue(self):
        return self.q_value
    
    def getText(self):
        return self.q_text
    
    def completeQuestion(self, complete, qs, cats):
        qs[(qs.index.isin(cats.getQuestionIndexes())) & (qs.clue_value == self.q_value)]['completed'] = 1
        
    def getAnswer(self):
        return self.q_answer
        
    def getQuestionCompleted(self):
        return self.q_complete