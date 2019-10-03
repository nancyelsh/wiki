from django.db import models

# Create your models here.
class Page(models.Model):
	"""docstring for Page"""
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)

	# def __init__(self, arg):
	# 	super( Page, self).__init__()
	# 	self.arg = arg
		