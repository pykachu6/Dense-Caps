from cryst_predict import model_maker_score
from cryst_predict import score_finder

def score_finder_tests():
    """Tests whether the output of the score_finder function returns  """
    inputs, outputs = model_maker_score(formula='LiOH')
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'
        
    
    inputs, outputs = model_maker_score(formula='LiOH', formation_e='2')
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'
        
    inputs, outputs = model_maker_score(formula='LiOH', formation_e='2', bandgap_input=2 )
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'
        
    inputs, outputs = model_maker_score(formula='LiOH', formation_e='2', bandgap_input=2, Volume='1')
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'
        
    inputs, outputs = model_maker_score(formula='LiOH', formation_e='2', bandgap_input=2, Volume='1', Nsites = 2)
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'
        
    inputs, outputs = model_maker_score(formula='LiOH', formation_e='2', bandgap_input=2, Volume='1', Nsites = 2, Density = 2 )
    scores = score_finder(inputs, outputs)
    
    for outs in list(outputs):
        print(outs)
        print(scores[outs])
        assert outs in scores, 'Expected output not found'
        assert isinstance(scores[outs], float), 'Incorrect type for score'