# Crystal Structure Class Predictive Tool

## Project Objective
Take in some number of parameters and predict a crystal structure for Li-ion electrodes.

It also predicts the missing inputs from the user. As an example, if the user inputs ‘Formula’, ‘Formation Energy’, and ‘Density’, the model will return the predicted crystal structure along with ’Nsites’, ‘Band Gap’, and ‘Volume’.

## Parameters
Each input/output parameter (and their units if applicable) are listed:

1. Formula
2. Formation Energy (eV)
3. Band Gap Energy (eV)
4. Number of Sites
5. Density (g/cubic cm)
6. Volume

## Requirements
Package crystpredict has the following main dependencies:

1. Python = 3.10
2. scikit-learn = 1.0.2

The detailed list of dependencies is reflected in the environment.yml file.

## Installation
The package crystpredict can be installed using following command:
```
conda env create -f environment.yml
conda activate crystpredict
```

## Testing
Tests located at <code/tests>

## Community Guidelines
We welcome any users of our tool to offer suggestions and fixes, feel free to [raise an issue](https://github.com/pykachu6/Dunce-Caps/issues/new) to submit any feature requests or report any bugs that come up.




