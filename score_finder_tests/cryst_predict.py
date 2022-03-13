import numpy as np
import matplotlib.pyplot as plt
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
################################################ Decision Tree ################################################

def decision_tree_builder(class_or_regress, X_train, y_train):
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
    
    #Building
    if class_or_regress == 'classifier':
        dt = DecisionTreeClassifier()
    else:
        dt = DecisionTreeRegressor()
    dt_random = RandomizedSearchCV(estimator = dt, param_distributions = parameters_dt, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    dt_random.fit(X_train, y_train)
    return dt_random.best_params_
################################################################################
################################################ Random Forest ################################################


def random_forest_builder(class_or_regress, X_train, y_train):
    
    #using this chunk below, find the best hyperparameters using random search, then output the MSE of crystal system 

    # for first parameter of function, write either "classifier" or "regressor"
    # The function will return optimal parameters for whether to bootstrap, max_depth, max_features, min_samples_leaf, 
    # min_samples_split, and n_estimators
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
    
    #Building
    if class_or_regress == 'classifier':
        rf = RandomForestClassifier()
    else:
        rf = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = parameters_rf, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    rf_random.fit(X_train, y_train)
    return rf_random.best_params_
################################################################################
################################################ Random Forest ################################################


def gradient_boosting_builder(class_or_regress, X_train, y_train):
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
    #Building

    if class_or_regress == 'classifier':
        gbc = GradientBoostingClassifier()
    else:
        gbc = GradientBoostingRegressor()
    gbc_random = RandomizedSearchCV(estimator = gbc, param_distributions = parameters_gbc, 
                                   n_iter = 10, cv = 3, verbose = 0, random_state=42, n_jobs = -1)
    gbc_random.fit(X_train, y_train)
    return gbc_random.best_params_

################################################################################
################################################################################
def model_maker_score(formula ='default',formation_e = '',bandgap_input = '', Nsites = '',Density = '',Volume=''):

    BigDataEnergy = pd.read_csv(r'lithium-ion batteries.csv')
    BigDataEnergy2 = BigDataEnergy[['Formation Energy (eV)', 'Band Gap (eV)','Nsites','Density (gm/cc)','Volume','Crystal System']].copy()

    permutations_list = []

    for i in range(0,len(BigDataEnergy['Formula'])):
        permutations_list.append(element_count(BigDataEnergy['Formula'][i]))

    formula_split = pd.DataFrame(permutations_list)

    concatenated_dataframes = pd.concat([formula_split, BigDataEnergy2], axis=1)

    stock_inputs = ['Formation Energy (eV)','Band Gap (eV)','Nsites','Density (gm/cc)','Volume']
    input_list = []

        
    if formation_e != '':
        input_list.append('Formation Energy (eV)')

    if bandgap_input != '':
        input_list.append('Band Gap (eV)')

    if Nsites != '':
        input_list.append('Nsites')

    if Density != '':
        input_list.append('Density (gm/cc)')

    if Volume != '':
        input_list.append('Volume')

    found = set(input_list) & set(stock_inputs)
    output_list = list(set(stock_inputs) - found)

    input_df = pd.concat([formula_split, BigDataEnergy2[input_list]], axis=1)
    output_df = pd.concat([BigDataEnergy2[output_list],BigDataEnergy2['Crystal System']], axis=1)
    
    
    ############  Ohh hey do the model training
    
    return input_df, output_df


################################################################################
################################################################################


def score_finder(input_df, output_df):
    
    score_dict_Tree = {}
    score_dict_Forest = {}
    score_dict_Boosting = {}

    for i in range(0,len(output_df.columns)):
        print(i)
        if output_df.columns[i] != 'Crystal System':
            X_train, X_test, y_train, y_test = train_test_split(input_df, output_df[output_df.columns[i]], test_size=0.10, random_state=42)

            params = random_forest_builder('regressor', X_train, y_train)
            reg_Forest = RandomForestRegressor( 
                n_estimators = params['n_estimators'],
                min_samples_split = params['min_samples_split'],
                min_samples_leaf = params['min_samples_leaf'],
                max_features = params['max_features'],
                max_depth = params['max_depth'],
                bootstrap = params['bootstrap'])
            score_Forest =np.round(cross_validate(reg_Forest, X_train, y_train, cv=3)['test_score'].mean(),3)


            params = gradient_boosting_builder('regressor', X_train, y_train)
            reg_Boosting = GradientBoostingRegressor(n_estimators = params['n_estimators'],
                max_depth = params['max_depth'],
                learning_rate = params['learning_rate'])
            score_Boosting = np.round(cross_validate(reg_Boosting, X_train, y_train, cv=3)['test_score'].mean(),3)

            params = decision_tree_builder('regressor', X_train, y_train)
            reg_Tree = DecisionTreeRegressor(
                min_samples_split = params['min_samples_split'],
                min_samples_leaf = params['min_samples_leaf'],
                max_features = params['max_features'],
                max_depth = params['max_depth'])
            score_Tree = np.round(cross_validate(reg_Tree, X_train, y_train, cv=3)['test_score'].mean(),3)

        else: 
            X_train, X_test, y_train, y_test = train_test_split(input_df, output_df[output_df.columns[i]], test_size=0.10, random_state=42)

            params = random_forest_builder('classifier', X_train, y_train)
            reg_Forest = RandomForestClassifier( 
                n_estimators = params['n_estimators'],
                min_samples_split = params['min_samples_split'],
                min_samples_leaf = params['min_samples_leaf'],
                max_features = params['max_features'],
                max_depth = params['max_depth'],
                bootstrap = params['bootstrap'])
            score_Forest =np.round(cross_validate(reg_Forest, X_train, y_train, cv=3)['test_score'].mean(),3)

            params = gradient_boosting_builder('classifier', X_train, y_train)
            reg_Boosting = GradientBoostingClassifier(n_estimators = params['n_estimators'],
                max_depth = params['max_depth'],
                learning_rate = params['learning_rate'])
            score_Boosting = np.round(cross_validate(reg_Boosting, X_train, y_train, cv=3)['test_score'].mean(),3)

            params = decision_tree_builder('classifier', X_train, y_train)
            reg_Tree = DecisionTreeClassifier(
                min_samples_split = params['min_samples_split'],
                min_samples_leaf = params['min_samples_leaf'],
                max_features = params['max_features'],
                max_depth = params['max_depth'])
            score_Tree = np.round(cross_validate(reg_Tree, X_train, y_train, cv=3)['test_score'].mean(),3)


        score_dict_Tree[output_df.columns[i]] = score_Tree
        score_dict_Boosting[output_df.columns[i]] = score_Boosting
        score_dict_Forest[output_df.columns[i]] = score_Forest

        ratings=[score_dict_Tree,score_dict_Boosting,score_dict_Forest]

    Overall_score = {}

    for i in range(0,len(list(ratings[0].keys()))):
        key_name = list(ratings[0].keys())[i]
        Overall_score[key_name] = np.round(np.mean([score_dict_Tree[key_name],score_dict_Boosting[key_name],score_dict_Forest[key_name]]),3)

    return Overall_score