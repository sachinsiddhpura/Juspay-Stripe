from django.db import models

# Create your models here.
class Pay(models.Model):
	full_name=models.CharField(max_length=230)
	email	=models.EmailField()
	stripe_id	=models.CharField(max_length=230)