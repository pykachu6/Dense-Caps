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
from sklearn.model_selection import cross_validate

################################################################################

element_list= ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co']

################################################################################

def get_occ_indices(str_to_search, str_target):
    """
    Returns all start indices of str_target in str_to_search as a list
    """
    
    occ_index_list =[]
    for index in range(len(str_to_search)):
        #print(str_to_search[index:index + len(str_target)])
        if str_to_search[index:index + len(str_target)] == str_target:
            occ_index_list.append(index)
        else:
            pass
    return occ_index_list

################################################################################

def get_parentheses(string_with_parentheses):
    """
    Returns a dict of open_parenthesis index:close_parenthesis index for all in given string. Does not work with nested parentheses
    """
    parentheses_index_list ={}
    for o_index in range(len(string_with_parentheses)):
        if string_with_parentheses[o_index] == '(':
            
            
            for c_index in range(o_index,len(string_with_parentheses)):
                #print(c_index)
                
                if string_with_parentheses[c_index] == ')':
                    #print(c_index)
                    
                    parentheses_index_list[o_index] = c_index
                    break
            
            
            
        else:
            pass
    return parentheses_index_list

################################################################################

def simple_count_in_instance(instance_index, string, element):
    """
    Returns the 1 or 2 digit number after a substring at a given index in a string, takes that as the number of elements of that type.
    If no number, takes number as 1.
    """
    
    counter = 0 
    try:
        #print(string[instance_index +len(element)])
        if string[instance_index +len(element)].isdigit() == False:
            counter += 1
        elif string[instance_index +len(element)].isdigit() == True:
            try:
                if string[instance_index +len(element)+1].isdigit() == False:
                    counter += int(string[instance_index +len(element)])
                elif string[instance_index +len(element)+1].isdigit() == True:
                    counter += int(string[instance_index+len(element):instance_index+len(element)+2])
            except IndexError:
                counter += int(string[instance_index +len(element)])

    except IndexError:
        counter += 1
    return counter

################################################################################
    
def element_count(formula_string):
    """
    Returns the sum of the counts of occurences of each element in element_list for a given formula string. Total should be equal to sum of numbers for element not in parentheses + sum of numbers*parentheses coefficient for all in parentheses.
    """
    parenthetical = get_parentheses(formula_string)
    
    ele_count = {}
    for elements in element_list:
        
        num_ele_n = 0
        occurences = get_occ_indices(formula_string, elements)
        for instance in occurences:
            coeff = 1
            inparentheses = False
            
            close_index = 0
            for open_par in parenthetical:
               
                
                if open_par < instance < parenthetical[open_par]:
                    inparentheses = True
                   
                    close_index = parenthetical[open_par]
                    
                    
                    
                    
                    
                else:
                    pass
                
            if inparentheses == False:
                pass
              
                
            else:


                try:
                    
                   
                    if formula_string[close_index + 1].isdigit() == True:
                        
                        
                        try:
                        
                            if formula_string[close_index + 2].isdigit() == True:
                                coeff = int(formula_string[close_index + 1:close_index + 3])
                               
                            else:
                                coeff = int(formula_string[close_index + 1])
                                
                        except IndexError:
                            coeff = int(formula_string[close_index + 1])
                       
                    else:
                        coeff = 1
                        
                except IndexError:
                    coeff = 1
                
               
            num_ele_n += simple_count_in_instance(instance, formula_string, elements)*coeff
            
                  
                    
        ele_count[elements] = num_ele_n
    return ele_count


################################################################################
