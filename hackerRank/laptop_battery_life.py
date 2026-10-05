#!/bin/python3

import math
import os
import random
import re
import sys


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def prepare_data():
    with open("trainingdata.txt", 'r', encoding='utf-8') as file:
        data = np.array([tuple((line.strip().split(','))) for line in file])
        
        # print(data[:, 0])
    return data

def train_model(data):
    np.set_printoptions(precision=2, suppress=True)
    
    X = data[:, 0].astype(float).reshape(-1, 1) # must always be 2d 
    y = data[:, 1].astype(float)
    
    # print(X)
    
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train ,y_train)
    
    test_score = model.score(X_test, y_test)
    # print(f"Test R² Score: {test_score:.4f}")
    
    return model
    
if __name__ == '__main__':
    # timeCharged = float(input().strip())
    
    data = prepare_data()
    train_model(data)