import predictor
import element_counter

test_formula = 'Li2MnSi3O8'

formation_e = 2
bandgap_input = 5
Nsites = 28
Density = 1.4
Volume = 5


Overall_value, Scores = predictor.value_finder(formula = test_formula, 
                                     formation_e = formation_e,
                                     bandgap_input = bandgap_input,
                                     Nsites = Nsites,
                                     Density = Density,
                                     Volume=Volume)
print(Overall_value)

print()

print(Scores)
