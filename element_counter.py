
################################################################################

element_list= ['Li', 'Si', 'Mn', 'Fe', 'O', 'Co']

################################################################################

def get_occ_indices(str_to_search, str_target):
    """Returns the index/indices in the str_to_search where the str_target occurs as a list"""
    occ_index_list =[]
    
    #Goes through each character, and checks if the index of that character plus the length of the target are the target
    for index in range(len(str_to_search)):
        
        if str_to_search[index:index + len(str_target)] == str_target:
            occ_index_list.append(index)
        else:
            pass
    return occ_index_list

################################################################################

def get_parentheses(string_with_parentheses):
    
    """Returns a dictionary of the form {open_parentheses_index:closed_parentheses_index} for a given string. PROBABLY DOESN"T WORK FOR NESTED PARENTHESES"""
    
    parentheses_index_list ={}
    
    #Check if each charater is an open parenthesis
    for o_index in range(len(string_with_parentheses)):
        if string_with_parentheses[o_index] == '(':
            
            #When it finds one, searches after the open to find a closed parenthesis. Assumes that the first one it finds is matched
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
    
    """Returns the (up to two digit) integer after a given element starting at instance index in string. If no integer after, returns 1""" 
    counter = 0 
    try:
        
        #Check if the character immediately after the element argument is a digit
        if string[instance_index +len(element)].isdigit() == False:
            #Set tp one if no digit
            counter += 1
        #If there is a digit, checks the next character after that to see if ti's a two-digit number
        #if not, returns value of 1st digit
        #If so, returns value of concatenated 1st and 2nd digits (i.e. 'Li24' would give an integer of 24)
        elif string[instance_index +len(element)].isdigit() == True:
            try:
                if string[instance_index +len(element)+1].isdigit() == False:
                    counter += int(string[instance_index +len(element)])
                elif string[instance_index +len(element)+1].isdigit() == True:
                    counter += int(string[instance_index+len(element):instance_index+len(element)+2])
            except IndexError:
                counter += int(string[instance_index +len(element)])
    
    #Index error handling: if we attempt to search past the end of the string, sets counter to one or the last character in the string
    except IndexError:
        counter += 1
    return counter

################################################################################
    
def element_count(formula_string):
    
    "For each element in element_list, returns the number of atoms of that element in the formula_string. NO COEFFICIENTS (after element or after parentheses) MORE THAN TWO CHARACTERS, NO NESTED PARENTHESES"""
    
    #Find parentheses
    parenthetical = get_parentheses(formula_string)
    
    ele_count = {}
    for elements in element_list:
        
        num_ele_n = 0
        
        #Find indices where the element name occurs
        occurences = get_occ_indices(formula_string, elements)
        for instance in occurences:
            #Coefficient to multiply by if in parentheses (1 if not in parentheses)
            coeff = 1
            inparentheses = False
            
            close_index = 0
            
            #Check if a given occurence of the element name is within parentheses
            for open_par in parenthetical:
               
                
                if open_par < instance < parenthetical[open_par]:
                    inparentheses = True
                    #close_index is the index of the closing parenthesis, which will be used to locate the coefficient of the parentheses
                    close_index = parenthetical[open_par]
                    
                    
                    
                    
                    
                else:
                    pass
                
            if inparentheses == False:
                pass
              
                
            else:
                try:
                    #Checks if the character after the closed parenthesis is a digit. 
                    #If it is, checks the next character in the same way
                    #Takes either no digit (coeff = 1), 1st character, or 1st and 2nd characters and converts it to int
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
                
            #number of elements_type due to the occurence. Number after element name times coefficient   
            num_ele_n += simple_count_in_instance(instance, formula_string, elements)*coeff
            
                  
                    
        ele_count[elements] = num_ele_n
    return ele_count


################################################################################
