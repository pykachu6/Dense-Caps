import numpy as np
import pandas as pd

from element_counter import get_occ_indices
from element_counter import get_parentheses
from element_counter import simple_count_in_instance
from element_counter import element_count

formula ='default'
formation_e = ''
bandgap_input = ''
Nsites = ''
Density = ''
Volume=''



formation_e = '11'
bandgap_input = '1'
Nsites = '1'
Density = '1'
Volume = ''
 


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


