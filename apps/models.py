from django.db import models

class AssessmentPlan(models.Model):
    # Static first column: Component (This column will hold the descriptions)
   # id = models.AutoField(primary_key=True)  
    duration = models.CharField(max_length=255)
    Weightage  = models.CharField(max_length=255)
    typeology  = models.CharField(max_length=255)
    Pattern  = models.CharField(max_length=255)
    schedule  = models.CharField(max_length=255)
    topicsovered  = models.TextField()
    
    class Meta:
        db_table= 'AssessmentPlan'