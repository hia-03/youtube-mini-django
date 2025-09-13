from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age=models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.first_name
    

class Post(models.Model):
    title=models.CharField( max_length=50)
    description=models.CharField( max_length=250)
    created_at=models.DateField( auto_now_add=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title