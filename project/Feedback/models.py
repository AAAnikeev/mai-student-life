from django.db import models

class FeedbackMessage(models.Model):
	"""docstring for FeedbackMessage"""
	text=models.TextField(max_length=500, default="")
	created_date = models.DateTimeField(auto_now_add=True)