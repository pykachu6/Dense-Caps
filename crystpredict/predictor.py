import numpy as np
import pandas as pd
import numbers
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor, GradientBoostingRegressor

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_validate

import crystpredict.element_counter
from crystpredict.element_counter import element_count
import crystpredict.hyperparameter
from crystpredict.hyperparameter import decision_tree_builder, random_forest_builder, gradient_boosting_builder

################################################ Model Maker ################################################

def model_maker_score(formula ='',formation_e = '',bandgap_input = '', Nsites = '',Density = '',Volume=''):
    """ Splits the datset into inputs and outputs, depending on what the user inputs. All uneneterd inputs are considered outputs"""
    
    BigDataEnergy = pd.read_csv('https://raw.githubusercontent.com/pykachu6/Dunce-Caps/main/lithium-ion%20batteries.csv')
    BigDataEnergy2 = BigDataEnergy[['Formation Energy (eV)', 'Band Gap (eV)','Nsites','Density (gm/cc)','Volume','Crystal System']].copy()

    # Makes a dataframe from the number of elements
    permutations_list = []    
    for i in range(0,len(BigDataEnergy['Formula'])):
        permutations_list.append(element_count(BigDataEnergy['Formula'][i]))
    formula_split = pd.DataFrame(permutations_list)

    # concatenates the element df and the sorted input df
    concatenated_dataframes = pd.concat([formula_split, BigDataEnergy2], axis=1)

    stock_inputs = ['Formation Energy (eV)','Band Gap (eV)','Nsites','Density (gm/cc)','Volume']
    input_list = []

    if formula == '':
        raise ValueError('No molecular formula entered')
        
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

    return input_df, output_df


################################################ Score Finder ################################################


def score_finder(input_df, output_df):
    """ Splits the input and output dfs from model_maker, finds best hyperparameters using randomized search and cross validation,
        returns the score and used hyperparemeters """
    
    # seeding lists
    score_dict_Tree = {}
    score_dict_Forest = {}
    score_dict_Boosting = {}

    parameters_dict_Tree = {}
    parameters_dict_Forest = {}
    parameters_dict_Boosting = {}
    big_data_params = {}
    
    for i in range(0,len(output_df.columns)):
        #finds if the output is a regressor or classifier
        if output_df.columns[i] != 'Crystal System':
            X_train, X_test, y_train, y_test = train_test_split(input_df, output_df[output_df.columns[i]], test_size=0.10, random_state=42)

            # chunk for random forest
            params = random_forest_builder('regressor', X_train, y_train)
            parameters_dict_Forest[output_df.columns[i]] = params
            reg_Forest = RandomForestRegressor(**params)
            score_Forest =np.round(cross_validate(reg_Forest, X_train, y_train, cv=3)['test_score'].mean(),3)

            # chunk for gradient booster
            params = gradient_boosting_builder('regressor', X_train, y_train)
            parameters_dict_Boosting[output_df.columns[i]] = params
            reg_Boosting = GradientBoostingRegressor(**params)
            score_Boosting = np.round(cross_validate(reg_Boosting, X_train, y_train, cv=3)['test_score'].mean(),3)

            # chunk decision tree
            params = decision_tree_builder('regressor', X_train, y_train)
            parameters_dict_Tree[output_df.columns[i]] = params
            reg_Tree = DecisionTreeRegressor(**params)
            score_Tree = np.round(cross_validate(reg_Tree, X_train, y_train, cv=3)['test_score'].mean(),3)

        else: 
            X_train, X_test, y_train, y_test = train_test_split(input_df, output_df[output_df.columns[i]], test_size=0.10, random_state=42)

            # chunk for random forest
            params = random_forest_builder('classifier', X_train, y_train)
            parameters_dict_Forest[output_df.columns[i]] = params
            reg_Forest = RandomForestClassifier(**params)
            score_Forest =np.round(cross_validate(reg_Forest, X_train, y_train, cv=3)['test_score'].mean(),3)

            # chunk for gradient booster
            params = gradient_boosting_builder('classifier', X_train, y_train)
            parameters_dict_Boosting[output_df.columns[i]] = params
            reg_Boosting = GradientBoostingClassifier(**params)
            score_Boosting = np.round(cross_validate(reg_Boosting, X_train, y_train, cv=3)['test_score'].mean(),3)

            # chunk decision tree
            params = decision_tree_builder('classifier', X_train, y_train)
            parameters_dict_Tree[output_df.columns[i]] = params
            reg_Tree = DecisionTreeClassifier(**params)
            score_Tree = np.round(cross_validate(reg_Tree, X_train, y_train, cv=3)['test_score'].mean(),3)


        score_dict_Tree[output_df.columns[i]] = score_Tree
        score_dict_Boosting[output_df.columns[i]] = score_Boosting
        score_dict_Forest[output_df.columns[i]] = score_Forest

        ratings = [score_dict_Tree,score_dict_Boosting,score_dict_Forest]

    big_data_params['Forest'] = parameters_dict_Forest
    big_data_params['Tree'] = parameters_dict_Tree
    big_data_params['Boosting'] = parameters_dict_Boosting
    
    # averages the score among all three estimators
    Overall_score = {}
    for i in range(0,len(list(ratings[0].keys()))):
        key_name = list(ratings[0].keys())[i]
        Overall_score[key_name] = np.round(np.mean([score_dict_Tree[key_name],score_dict_Boosting[key_name],score_dict_Forest[key_name]]),3)

    return Overall_score , big_data_params


################################################ Predictor ################################################


def value_finder(formula = '', formation_e = '',bandgap_input = '', Nsites = '',Density = '',Volume=''):
    """ Uses what the user inputs to predict all missing inputs and crystal structure """
    
    # sorts the inputs 
    test_input = element_count(formula)
    if formation_e != '':
        test_input['Formation Energy (eV)'] = formation_e

    if bandgap_input != '':
        test_input['Band Gap (eV)'] = bandgap_input

    if Nsites != '':
        test_input['Nsites'] = Nsites 

    if Density != '':
        test_input['Density (gm/cc)'] = Density

    if Volume != '':
        test_input['Volume'] = Volume
    #slams the data for one input
    tester_input = pd.DataFrame(data=[test_input])    
    
    #makes the model
    input_df, output_df = model_maker_score(formula = formula,formation_e = formation_e ,
                                            bandgap_input = bandgap_input, Nsites = Nsites,
                                            Density = Density,Volume = Volume)
    #finds the scores and best hyperparameters
    Scores, parameters = score_finder(input_df, output_df)
    
    
    value_dict_Tree = {}
    value_dict_Forest = {}
    value_dict_Boosting = {}

    for i in range(0,len(output_df.columns)):

        if output_df.columns[i] != 'Crystal System':
            X_train,y_train = input_df, output_df[output_df.columns[i]] # now uses all data

            params = parameters['Forest'][output_df.columns[i]]
            reg_Forest = RandomForestRegressor(**params).fit(X_train, y_train)
            y_predict_Forest = reg_Forest.predict(tester_input)

            params = parameters['Boosting'][output_df.columns[i]]
            reg_Boosting = GradientBoostingRegressor(**params).fit(X_train, y_train)
            y_predict_Boosting = reg_Boosting.predict(tester_input)

            params = parameters['Tree'][output_df.columns[i]]
            reg_Tree = DecisionTreeRegressor(**params).fit(X_train, y_train)
            y_predict_Tree = reg_Tree.predict(tester_input)

        else: 
            X_train,y_train = input_df, output_df[output_df.columns[i]] # now uses all data

            params = parameters['Forest'][output_df.columns[i]]
            reg_Forest = RandomForestClassifier(**params).fit(X_train, y_train)
            y_predict_Forest = reg_Forest.predict(tester_input)

            params = parameters['Boosting'][output_df.columns[i]]
            reg_Boosting = GradientBoostingClassifier(**params).fit(X_train, y_train)
            y_predict_Boosting = reg_Boosting.predict(tester_input)

            params = parameters['Tree'][output_df.columns[i]]
            reg_Tree = DecisionTreeClassifier(**params).fit(X_train, y_train)
            y_predict_Tree = reg_Tree.predict(tester_input)

        value_dict_Tree[output_df.columns[i]] = (y_predict_Tree)
        value_dict_Boosting[output_df.columns[i]] = (y_predict_Boosting)
        value_dict_Forest[output_df.columns[i]] = (y_predict_Forest)

        ratings = [value_dict_Tree,value_dict_Boosting,value_dict_Forest]

        
        # averages the predicted value among all three estimators
        Overall_value = {}
        for i in range(0,len(list(ratings[0].keys()))):
            key_name = list(ratings[0].keys())[i]

            lst = [value_dict_Tree[key_name],value_dict_Boosting[key_name],value_dict_Forest[key_name]]
            lst = [item for sublist in lst for item in sublist]

            if key_name != 'Crystal System':
                Overall_value[key_name] = np.round(np.mean(lst),3)

            else:
                Overall_value[key_name] = max(set(lst), key=lst.count)


    return Overall_value, Scores


