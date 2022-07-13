from django.db import models
from datetime import datetime

# Create your models here.
class notes(models.Model):
	title  = models.CharField(max_length=50)
	date = models.DateTimeField(default = datetime.now)
	write = models.TextField()

	def __str__(self):
		return self.title

