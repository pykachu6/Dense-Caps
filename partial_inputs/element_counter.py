
################################################################################

element_list= ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co']

################################################################################

def get_occ_indices(str_to_search, str_target):
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
