from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import CHD
from .serializers import CHDSerializer
import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.shortcuts import render
import joblib
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"



class peopleView(viewsets.ModelViewSet):
    queryset = CHD.objects.all()
    serializer_class = CHDSerializer

def ohevalue(df):
    one_col =joblib.load("class/encoder.pkl")
    cat_columns=['Cigs_Per_Day','BPMeds','totChol','BMI','heartRate','Glucose']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict={}
    for i in one_col:
        if i in df_processed.columns:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
    newdf=pd.DataFrame(newdict)
    return newdf
    
def deploy(unit):
    try:
        model = joblib.load("class/mmodel.pkl")
        scaler = joblib.load("class/scaler.pkl")
        X=scaler.transform(unit)
        y_pred= model.predict(X)
        y_pred=(y_pred>0.58)
        newdf = pd.DataFrame(y_pred, columns=["TenYearCHD"])
        newdf = newdf.replace({True:"Be Carefull😕, You Have a Chance of getting CHD in next ten years, Kindly Consult a Doctor.", False:"Good News🙂, You don't have a chance of getting CHD in next ten Years"})
        return newdf.values[0][0]
    except ValueError as e:
        return Response(e.args[0])

def cxcontact(request):
    if  request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            Gender = form.cleaned_data['Gender']
            Age = form.cleaned_data['Age']
            # Education = form.cleaned_data['Education']
            Diabetes = form.cleaned_data['Diabetes']
            Glucose = form.cleaned_data['Glucose']
            Current_Smoker = form.cleaned_data['Current_Smoker']
            Cigs_Per_Day  = form.cleaned_data['Cigs_Per_Day'] 
            BPMeds = form.cleaned_data['BPMeds']
            totChol = form.cleaned_data['totChol']
            DiaBP = form.cleaned_data['DiaBP']
            Systolic_BP = form.cleaned_data['Systolic_BP']
            Prevalent_Stroke = form.cleaned_data['Prevalent_Stroke']
            Prevalent_Hypertension  = form.cleaned_data['Prevalent_Hypertension']
            BMI = form.cleaned_data['BMI']
            heartRate = form.cleaned_data['heartRate']
            Glucose = form.cleaned_data['Glucose']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = deploy(ohevalue(df))
            # print(ohevalue(df))
            messages.success(request,'{}'.format(answer))  
            # print(Gender, Age, BMI)
       
    form = MyForm()
    return render(request,"MyForm/form.html",{'form':form})    
