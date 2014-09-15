from django.db import models

# Create your models here.

class Wisdom(models.Model):
	wisdom_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date said')

	def __unicode__(self):
		return self.wisdom_text