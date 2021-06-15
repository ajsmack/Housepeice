from django.shortcuts import render
from.import ml_predict

def home(request):
    return render(request,"index.html")

def result(request):
    lotsize = int(request.GET["lotsize"])
    bathrms = int(request.GET["bathrms"])
    stories = int(request.GET["stories"])
    driveway = int(request.GET["driveway"])
    recroom = int(request.GET["recroom"])  
    fullbase = int(request.GET["fullbase"])
    gashw = int(request.GET["gashw"])
    airco = int(request.GET["airco"])
    garagepl = int(request.GET["garagepl"])
    prefarea = int(request.GET["prefarea"])
    
    prediction = ml_predict.prediction_model(lotsize,bathrms,stories,driveway,recroom,fullbase,gashw,airco,garagepl,prefarea)
    return render(request,"index.html", {'prediction':prediction})
