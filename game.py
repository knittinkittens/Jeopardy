#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:19:01 2017

"""

#==============================================================================
# Package imports
#==============================================================================
import os
os.chdir('/Volumes/Lexar/Jeopardy/')

import pandas as pd
from random import randint
import threading
pd.options.mode.chained_assignment = None

from show import Show
from category import Category
from question import Question
from player import Player

#==============================================================================
# Base dataset containing questions, values, categories, and answers
#==============================================================================
qs = pd.read_csv('/Volumes/Lexar/Jeopardy/All Jeopardy Questions.csv').reset_index()
qs = qs[['index', 'show', 'categories', 'question', 'answer', 'daily_double', 'q_type', 'clue_value']]
qs = qs.drop_duplicates()
qs['completed'] = 0

    
def user_buzz():
    global response
    response = input("You have 10 seconds to type \'buzz\'...\n")
    
def user_answer():
    global answer
    answer = input('Your answer: ')
        
def main():
    
    print('Welcome to Jeopardy!\n\n')
    
    user = input("Please enter your Player name: ")
    user = Player(user)
    
    seed = randint(0, len(qs.show.unique()))
    show = Show(list(qs.show.unique())[seed], qs)
    print('\nYour Round 1 categories are: \n\t', '\n\t'.join(list(show.getCategories())))
    cat = input("Please pick a category: ")
    cat = Category(show, cat, qs)
    question = input('Please pick a question value from: \n\t' + '\n\t'.join(list(map(str, cat.getValues()))) + '\n')
    
    question = int(question)
    question = Question(cat, question, qs)
    print(question.getText())
    
    response = None
    buzz = threading.Thread(target=user_buzz)
    buzz.daemon = True
    buzz.start()
    buzz.join(10)
    if response is None:
        print('You missed this question :(')
        print('\nThe correct answer is: {0}'.format(question.getAnswer()))
    else:
        answer = None
        ans = threading.Thread(target=user_answer)
        ans.daemon = True
        ans.start()
        ans.join(10)
        if answer != question.getAnswer():
            user.subtractPoints(question.getValue())
            print("That answer is incorrect.\nThe correct answer is: {0}".format(question.getAnswer()))
        else:
            user.addPoints(question.getValue())
            print("Correct!")

    question.completeQuestion(1, qs, cat)
    cat.setQuestions(qs)
    cat.setValues(qs)

        
        
        
        
        
        
        
        