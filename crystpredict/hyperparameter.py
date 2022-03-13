import numpy as np
import pandas as pd
import numbers
from sklearn.model_selection import train_test_split
from sklearn import tree
import sklearn
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn import neighbors
from sklearn.model_selection import RandomizedSearchCV
from prettytable import PrettyTable
from sklearn.model_selection import cross_validate

################################################ Decision Tree ################################################

# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(3, 15, num = 13)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]

# Create the random grid
parameters_dt = {'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}

def decision_tree_builder(class_or_regress, X_train, y_train):
    if class_or_regress == 'classifier':
        dt = DecisionTreeClassifier()
    else:
        dt = DecisionTreeRegressor()
    dt_random = RandomizedSearchCV(estimator = dt, param_distributions = parameters_dt, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    dt_random.fit(X_train, y_train)
    return dt_random.best_params_

################################################ Random Forest ################################################


#using this chunk below, find the best hyperparameters using random search, then output the MSE of crystal system 

# for first parameter of function, write either "classifier" or "regressor"
# The function will return optimal parameters for whether to bootstrap, max_depth, max_features, min_samples_leaf, 
# min_samples_split, and n_estimators

from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 10, stop = 100, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(3, 15, num = 13)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
parameters_rf = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}


def random_forest_builder(class_or_regress, X_train, y_train):
    if class_or_regress == 'classifier':
        rf = RandomForestClassifier()
    else:
        rf = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = parameters_rf, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    rf_random.fit(X_train, y_train)
    return rf_random.best_params_


################################################ Boosting ################################################

# Number of estimators in GBC    
n_estimators = [int(x) for x in np.linspace(start = 10, stop = 100, num = 10)]
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(3, 15, num = 13)]
max_depth.append(None)
# Learning rate
learning_rate = [0.001,0.001,0.01,0.1]

parameters_gbc = {'n_estimators': n_estimators,
               'max_depth': max_depth,
               'learning_rate': learning_rate}

def gradient_boosting_builder(class_or_regress, X_train, y_train):
    if class_or_regress == 'classifier':
        gbc = GradientBoostingClassifier()
    else:
        gbc = GradientBoostingRegressor()
    gbc_random = RandomizedSearchCV(estimator = gbc, param_distributions = parameters_gbc, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    gbc_random.fit(X_train, y_train)
    return gbc_random.best_params_