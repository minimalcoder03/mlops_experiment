import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

test_data = pd.read_csv('test.csv')
train_data = pd.read_csv('train.csv')

X_train = train_data['x'].values.reshape(-1, 1)
