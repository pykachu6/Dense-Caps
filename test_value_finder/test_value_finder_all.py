
import numpy as np
import pandas as pd
import numbers
import sklearn

from element_counter import get_occ_indices
from element_counter import get_parentheses
from element_counter import simple_count_in_instance
from element_counter import element_count

from hyperparameter import decision_tree_builder, random_forest_builder, gradient_boosting_builder
from predictor import model_maker_score, score_finder, value_finder


from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn import neighbors
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_validate

def test_1_value_finder():
    
    #Test 1: One input as formula
    Overall_value, Scores = value_finder(formula = 'Li2MnSi3O8')
    
    list_ = sorted(['Band Gap (eV)', 'Crystal System', 'Density (gm/cc)', 
                    'Formation Energy (eV)', 'Nsites', 'Volume'])
    
    
    assert list_ == sorted(list(Overall_value.keys())), 'Unexpected or missing key'
    assert len(Overall_value) == len (Scores) , 'The output of values and scores do not match'
    
                #Testing individual entries of each element in the dictionary
    for k in Overall_value:
    
        assert type(Overall_value.get(k)) is float or str , 'Unexpected value type in dictionary'
        
     #Using a test case as a quantitative check   
    assert sorted(Overall_value) == sorted({'Nsites': 32.993,
                              'Formation Energy (eV)': -2.866,
                              'Density (gm/cc)': 2.618,
                              'Volume': 366.693,
                              'Band Gap (eV)': 2.87,
                              'Crystal System': 'monoclinic'}), 'Unexpected value in key'
        
def test_2_value_finder():       
        
    #Test 2: Two inputs as formula and formation energy
    
    Overall_value, Scores = value_finder(formula = 'Li2MnSi3O8', 
                                           formation_e = 2)
    
    list_ = sorted(['Band Gap (eV)', 'Crystal System', 'Density (gm/cc)', 
                     'Nsites', 'Volume'])
    
    
    assert list_ == sorted(list(Overall_value.keys())) , 'Unexpected or missing key'
    assert len(Overall_value) == len (Scores) , 'The output of values and scores do not match'
    
    for k in Overall_value:
    
        assert type(Overall_value.get(k)) is float or str , 'Unexpected value type in dictionary'
        
        
    #Using a test case as a quantitative check   
    assert sorted(Overall_value) == sorted({'Density (gm/cc)': 3.503,
                                             'Nsites': 33.491,
                                             'Volume': 428.888,
                                             'Band Gap (eV)': 0.803,
                                             'Crystal System': 'monoclinic'}), 'Unexpected value in key'

def test_3_value_finder():
     #Test 3: Three inputs as formula, formation energy, and bandgap input
    Overall_value, Scores = value_finder(formula = 'Li2MnSi3O8', 
                                           formation_e = 2, 
                                           bandgap_input = 5)
    
    list_ = sorted(['Crystal System', 'Density (gm/cc)', 
                     'Nsites', 'Volume'])
    
    
    assert list_ == sorted(list(Overall_value.keys())), 'Unexpected or missing key'
    assert len(Overall_value) == len (Scores) , 'The output of values and scores do not match'
    
    for k in Overall_value:
    
        assert type(Overall_value.get(k)) is float or str , 'Unexpected value type in dictionary'
        
    #Using a test case as a quantitative check       
    assert sorted(Overall_value) == sorted({'Density (gm/cc)': 2.94,
                                             'Volume': 502.394,
                                             'Nsites': 32.457,
                                             'Crystal System': 'monoclinic'}) , 'Unexpected value in key'
def test_4_value_finder():
    #Test 4: Three inputs as formula, formation energy, bandgap input, density
    Overall_value, Scores = value_finder(formula = 'Li2MnSi3O8', 
                                           formation_e = 2, 
                                           bandgap_input = 5,
                                           Density = 1.4)
    
    list_ = sorted(['Crystal System', 
                     'Nsites', 'Volume'])
    
    
    assert list_ == sorted(list(Overall_value.keys())), 'Unexpected or missing key'
    assert len(Overall_value) == len (Scores) , 'The output of values and scores do not match'
    
    for k in Overall_value:
    
        assert type(Overall_value.get(k)) is float or str , 'Unexpected value type in dictionary'
        
    assert sorted(Overall_value) == sorted({'Volume': 460.937, 
                                         'Nsites': 32.674, 
                                         'Crystal System': 'monoclinic'}),'Unexpected value in key'
    
def test_5_value_finder():
    #Test 5: Three inputs as formula, formation energy, bandgap input, density, Volume
    Overall_value, Scores = value_finder(formula = 'Li2MnSi3O8', 
                                           formation_e = 2, 
                                           bandgap_input = 5,
                                           Density = 1.4,
                                           Volume = 5)
    
    list_ = sorted(['Crystal System', 
                     'Nsites', ])
    
    
    assert list_ == sorted(list(Overall_value.keys())), 'Unexpected or missing key'
    assert len(Overall_value) == len (Scores) , 'The output of values and scores do not match'
    
    for k in Overall_value:
    
        assert type(Overall_value.get(k)) is float or str , 'Unexpected value type in dictionary'
        
    assert sorted(Overall_value) == sorted({'Nsites': 14.338, 
                                         'Crystal System': 'orthorhombic'}),'Unexpected value in key'
    
    
    
