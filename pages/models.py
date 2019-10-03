from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
	"""docstring for Page"""
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)

	# def __init__(self, arg):
	# 	super( Page, self).__init__()
	# 	self.arg = arg

	def get_absolute_url(self):
		# return "detail/%s/" % self.id
		return reverse("page-detail", kwargs={"page_id": self.id})
		