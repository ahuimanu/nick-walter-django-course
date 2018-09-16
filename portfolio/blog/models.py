from django.db import models

# Create your models here.

# create blog model
# add blog app to settings
# create migration
# run migration
# add to admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')