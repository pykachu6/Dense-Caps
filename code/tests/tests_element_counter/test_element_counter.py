#These are the full bank of tests for the element counter functions
import pandas as pd

#Importing functions
from element_counter import get_occ_indices
from element_counter import get_parentheses
from element_counter import simple_count_in_instance
from element_counter import element_count

#The following are functions to test the element counter functions

def test_get_occ_indices():
    
    #Testing that we get the expected indices for some input formula 'Li4Mn2Si3O10'
    assert get_occ_indices('Li4Mn2Si3O10', 'Li' )[0] == 0 , "Lithium is not where it is expected in the formula"
    assert get_occ_indices('Li4Mn2Si3O10', 'Mn' )[0] == 3 , "Manganese is not where it is expected in the formula"
    assert get_occ_indices('Li4Mn2Si3O10', 'Si')[0] == 6 , "Silicon is not where it is expected in the formula"
    assert get_occ_indices('Li4Mn2Si3O10', 'O')[0] == 9 , "Oxygen is not where it is expected in the formula"

    #Testing that we get the expected indices for some input formula 'Li4Fe2Si3O10'
    assert get_occ_indices('Li4Fe2Si3O10', 'Li' )[0] == 0 , "Lithium is not where it is expected in the formula"
    assert get_occ_indices('Li4Fe2Si3O10', 'Fe' )[0] == 3 , "Manganese is not where it is expected in the formula"
    assert get_occ_indices('Li4Fe2Si3O10', 'Si')[0] == 6 , "Silicon is not where it is expected in the formula"
    assert get_occ_indices('Li4Fe2Si3O10', 'O')[0] == 9 , "Oxygen is not where it is expected in the formula"    
    
    
    #Testing the output types of the function
    assert isinstance('Li4Mn2Si3O10', str) , 'The input of the funciton is not a string'
    assert isinstance(get_occ_indices('Li4Mn2Si3O10', 'Li' ), list) , 'The output of get_occ_indices() is not a list'
    
    
    #Testing to make sure odd ball elements are not in the input formulas
    assert 'U' not in 'Li4Mn2Si3O10' , 'Unexpected element in the input'
    assert 'P' not in 'Li4Mn2Si3O10' , 'Unexpected element in the input'
    assert 'Pb' not in 'Li4Mn2Si3O10' , 'Unexpected element in the input'
    assert 'V' not in 'Li4Mn2Si3O10' , 'Unexpected element in the input'

    
def test_get_parentheses():
    
    assert isinstance(get_parentheses('Li7Mn3(SiO6)2'), dict) , 'The output of get_parentheses() is not a string'
    assert isinstance(get_parentheses('LiFe(Si2O5)2'), dict) , 'The output of get_parentheses() is not a string'
    assert len(get_parentheses('LiFe(Si2O5)2')) == 1 , 'Unexpected output length'
    assert len(get_parentheses('Li4Mn2Si3O10')) == 0 , "There is an unexpected parenthesis in this group"
    
    
    
def test_element_count():
    
    element_list= ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co']
    
    #Test entire type of element_count
    assert isinstance(element_count('Li7Mn3(SiO6)2'), dict) , 'The returned type is not a dictionary'
    
    #test correct and all elements are returned in the dictionary
    assert all(k in element_count('Li7Mn3(SiO6)2') for k in element_list), 'Unexpected element in formula'
    
    
    #testing each value of the dictionary is an interget
    dict_ = element_count('Li7Mn3(SiO6)2')
    sum_ = []
    list_ = []
    
    #This for loop tests the keys of the dictionary
    for key in dict_.items() :
    
      
        list_.append(key[0])

    assert all(isinstance(n, str) for n in list_),'The keys in the dictionary are not strings'  
    
    #The following for loop seperates out the values in the dictionary and tests them
    
    for k in dict_:
        
        #Test sum of the values in dictionary to make sure number of atoms in formula is correct
        sum_.append(dict_.get(k))
        
        #Test each value type in dictionary is not float
        assert type(dict_.get(k)) is not float , 'The value in the dictionary is a float'
        
        #Test each value type in dictionary is not string
        assert type(dict_.get(k)) is not str , 'The value in the dictionary is a string'
        
        #Test each value type in dictionary is not a list
        assert type(dict_.get(k)) is not list , 'The value in the dictionary is a list'


        #Test each value type in dictionary is an interger
        assert type(dict_.get(k)) is int , 'The value is not an interger'
    
    
    assert sum(sum_)== 24, 'Incorrect numbers of atoms in material formula'
    
    
