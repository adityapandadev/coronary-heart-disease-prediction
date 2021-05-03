from django import forms
from .models import CHD
# from django.forms import ModelForm

# class MyForm(ModelForm):
#     class Meta:
#         model = CHD
#         fields = ["Age","totChol","DiaBP","Systolic_BP","Cigs_Per_Day","BMI","heartRate","Glucose","Current_Smoker","BPMeds","Diabetes","Gender","Prevalent_Stroke","Prevalent_Hypertension"]

# 
class MyForm(forms.Form):

    Age=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Age','class':'w3-hover-sand'}))
    totChol = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Total Cholesterol','class':'w3-hover-sand'}))
    DiaBP = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Diastolic blood pressure','class':'w3-hover-sand'}))
    Systolic_BP = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Systolic Blood Pressure','class':'w3-hover-sand'}))
    Cigs_Per_Day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'cigerates Per Day','class':'w3-hover-sand'}))
    BMI =  forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Body mass index','class':'w3-hover-sand'}))
    heartRate = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Heart-rate','class':'w3-hover-sand'}))
    Glucose = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Glucose level in body','class':'w3-hover-sand'}))
    # Education = forms.ChoiceField(choices=[('1','10th'), ('2','12th'),('3','graduated'),('4','post-graduated')])
    Current_Smoker = forms.ChoiceField(choices=[('1','Yes'),('0','NO')])
    BPMeds = forms.ChoiceField(choices=[('1','Yes'),('0','NO')])
    Diabetes = forms.ChoiceField(choices=[('1','Yes'),('0','NO')])
    Gender=forms.ChoiceField(choices=[('1','male'),('0','female')])
    Prevalent_Stroke = forms.ChoiceField(choices=[('1','Yes'),('0','NO')])
    Prevalent_Hypertension = forms.ChoiceField(choices=[('1','Yes'),('0','NO')])

