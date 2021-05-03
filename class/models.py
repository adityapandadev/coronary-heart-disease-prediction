from django.db import models

# Create your models here.
class CHD(models.Model):
    # EUDCATION_CHOICES =(('1','10th'), ('2','12th'),('3','graduated'),('4','post-graduated'))
    SMOKER_CHOICES = (('1','Yes'),('0','NO'))
    BPMeds_CHOICES =  (('1','Yes'),('0','NO'))
    DIBT_CHOICES = (('1','Yes'),('0','NO'))
    CHD_CHOICES = (('1','Yes'),('0','NO'))
    STROKE_CHOICES = (('1','Yes'),('0','NO'))
    HYP_CHOICES = (('1','Yes'),('0','NO'))
    GENDER_CHOICES = (('1','Male'),('0','Female'))
    
    Gender=models.CharField(max_length=6, choices = GENDER_CHOICES)
    Age=models.IntegerField(default=0)
    # Education = models.CharField(max_length=15, choices=EUDCATION_CHOICES) 
    Current_Smoker = models.CharField(max_length=3, choices=SMOKER_CHOICES)
    Cigs_Per_Day = models.IntegerField(default=0)
    BPMeds = models.CharField(max_length=3, choices = BPMeds_CHOICES)
    Prevalent_Stroke = models.CharField(max_length=3, choices = STROKE_CHOICES)
    Prevalent_Hypertension = models.CharField(max_length=3, choices = HYP_CHOICES)
    Diabetes = models.CharField(max_length=3, choices = DIBT_CHOICES)
    totChol = models.IntegerField(default=0)
    DiaBP = models.IntegerField(default=0)
    Systolic_BP = models.FloatField(default=0)
    BMI =  models.FloatField(default=0)
    heartRate = models.IntegerField(default=0)
    Glucose = models.IntegerField(default=0)

    def __str__(self):
        return self.Gender, self.Prevalent_Hypertension