

import numpy as np
import pandas as pd

from element_counter import get_occ_indices
from element_counter import get_parentheses
from element_counter import simple_count_in_instance
from element_counter import element_count
from model_maker import model_maker_score

def test_model_maker_score():
    
    #Testing one input matching the model maker score seperator
    output_list1 = ['Band Gap (eV)', 'Crystal System', 'Density (gm/cc)', 'Formation Energy (eV)', 'Nsites', 'Volume']
    input_list1 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co']
    
    input1 , output1 = model_maker_score(formula ='Li4MnSi2O7')
        
    assert sorted(output1.columns.values.tolist()) == sorted(output_list1) , 'There is an unexpected output variable name'
    assert input1.columns.values.tolist() == input_list1 , 'There is an unexpected input variable name'
    
    
    #Testing two inputs match the model maker score seperator
    output_list2 = ['Volume', 'Band Gap (eV)', 'Nsites', 'Density (gm/cc)', 'Crystal System']
    input_list2 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co', 'Formation Energy (eV)']
    
    input2 , output2 = model_maker_score(formula ='Li4MnSi2O7', formation_e = 2)
     
    
    assert sorted(output2.columns.values.tolist()) == sorted(output_list2) , 'There is an unexpected output variable name'
    assert input2.columns.values.tolist() == input_list2 , 'There is an unexpected input variable name'

    
    #Testing 3 inputs match the model maker seperator
    output_list3 = ['Volume', 'Nsites', 'Density (gm/cc)', 'Crystal System']
    input_list3 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co', 'Formation Energy (eV)', 'Band Gap (eV)']
    
    input3 , output3 = model_maker_score(formula ='Li4MnSi2O7', formation_e = 2, bandgap_input = 2)

    assert sorted(output3.columns.values.tolist()) == sorted(output_list3) , 'There is an unexpected output variable name'
    assert input3.columns.values.tolist() == input_list3 , 'There is an unexpected input variable name'
    
    
    #Testing 4 inputs match the model maker seperator
    output_list4 = ['Volume', 'Density (gm/cc)', 'Crystal System']
    input_list4 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co', 'Formation Energy (eV)', 'Band Gap (eV)','Nsites']
    
    input4 , output4 = model_maker_score(formula ='Li4MnSi2O7', formation_e = 2, bandgap_input = 2, Nsites = 16)
   
    assert sorted(output4.columns.values.tolist()) == sorted(output_list4) , 'There is an unexpected output variable name'
    assert input4.columns.values.tolist() == input_list4 , 'There is an unexpected input variable name'
    
    
    #Testing 5 inputs match the model maker seperator
    output_list5 = ['Volume', 'Crystal System']
    input_list5 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co', 'Formation Energy (eV)', 'Band Gap (eV)','Nsites','Density (gm/cc)']
    
    input5 , output5 = model_maker_score(formula ='Li4MnSi2O7', formation_e = 2,
                                         bandgap_input = 2, Nsites = 16, Density = 2.8)
        
    assert sorted(output5.columns.values.tolist()) == sorted(output_list5) , 'There is an unexpected output variable name'
    assert input5.columns.values.tolist() == input_list5 , 'There is an unexpected input variable name'
    
    #Testing 6 inputs match the model maker seperator
    output_list6 = ['Crystal System']
    input_list6 = ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co', 'Formation Energy (eV)', 
                   'Band Gap (eV)','Nsites','Density (gm/cc)','Volume']
    
    input6 , output6 = model_maker_score(formula ='Li4MnSi2O7', formation_e = 2,
                                         bandgap_input = 2, Nsites = 16, Density = 2.8, Volume = 175)
        
    assert output6.columns.values.tolist() == output_list6 , 'There is an unexpected output variable name'
    assert input6.columns.values.tolist() == input_list6 , 'There is an unexpected input variable name'
    
    #testing lengths of each output
    
    assert len(output1) == len(input1) , 'The lenghts of the inputs and outputs do not match'
    assert len(output2) == len(input2) , 'The lenghts of the inputs and outputs do not match'
    assert len(output3) == len(input3) , 'The lenghts of the inputs and outputs do not match'
    assert len(output4) == len(input4) , 'The lenghts of the inputs and outputs do not match'
    assert len(output5) == len(input5) , 'The lenghts of the inputs and outputs do not match'
    assert len(output6) == len(input6) , 'The lenghts of the inputs and outputs do not match'

    #Test the type of each input
    
 
    assert isinstance(output1['Volume'][0], float) , 'The Volume output type is not a float'
    assert isinstance(output1['Density (gm/cc)'][0], float) , 'The Density output type is not float'
    assert isinstance(output1['Nsites'][0], np.int64) , 'The Nsites output type is not an interger'
    assert isinstance(output1['Formation Energy (eV)'][0], float) , 'The Formation Energy output type is not a float'
    assert isinstance(output1['Band Gap (eV)'][0], float) , 'The Formation Energy output type is not a float'

    
    
    
