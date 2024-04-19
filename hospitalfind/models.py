from django.db import models
from django.utils import timezone
# Create your models here.

class logindetails(models.Model):
	user = models.CharField(max_length = 15)
	password = models.CharField(max_length = 10)
	email = models.CharField(max_length = 30,primary_key = True)
	
class hospitaldetails(models.Model):
	verbose_name_plural = "Hospital Details"
	Hospital_id = models.CharField(max_length = 10)
	Hospital_Name = models.CharField(max_length = 100)
	Address = models.CharField(max_length = 50)
	Helpline_number = models.CharField(max_length = 100)
	Description = models.TextField()
	class hospital_choice(models.TextChoices):
		Public = "Public"
		Private = "Private"

	Hospital_type = models.CharField(max_length = 50,choices = hospital_choice.choices,default = hospital_choice.Public)
	Hospital_image = models.ImageField(upload_to ='static/findhospital/recipe_img', max_length=255, null=True) 
	
	def __str__(self):
		return self.Hospital_Name