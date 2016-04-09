from django.db import models

# Create your models here.
class pages(models.Model):
	page_id = models.BigIntegerField()
	page_name = models.CharField(max_length = 100 , default='')
	page_category = models.CharField(max_length = 100 , default='')
	page_posts_json = models.TextField(max_length=8000 , default='')
	page_likes = models.IntegerField()
	page_json = models.TextField(max_length = 8000 , default = "")
	def __str__(self):
		return self.page_name


class twitter(models.Model):
	twitter_json = models.TextField(max_length = 8000 , default = "")