from django.db import models

class camp(models.Model):
	name = models.CharField(max_length = 500)
	xcor = models.DecimalField(max_digits=10, decimal_places=4, default="")
	ycor = models.DecimalField(max_digits=10, decimal_places=4, default="")
	capacity = models.IntegerField(default=200)

	def __str__(self):
   		return self.name