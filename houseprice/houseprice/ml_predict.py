
def prediction_model(lotsize,bathrms,stories,driveway,recroom,fullbase,gashw,airco,garagepl,prefarea):
    import pickle
    import numpy as np
    x = [[lotsize,bathrms,stories,driveway,recroom,fullbase,gashw,airco,garagepl,prefarea]]
    regression_model = pickle.load(open('regression_model.sav','rb'))
    prediction = regression_model.predict(x)
    prediction = np.asscalar(prediction)
    prediction = np.round(prediction,decimals =2)
    return prediction

