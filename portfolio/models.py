from django.db import models
from django.utils.timezone import now

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField(max_length=255)
    tech_stack = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='video',null=True)
    
class Education(models.Model):
    course_name = models.CharField(max_length=150)
    course_year = models.CharField(max_length=30)
    institute_name = models.CharField(max_length=100)
    cgpa_or_percentage = models.FloatField()
    
