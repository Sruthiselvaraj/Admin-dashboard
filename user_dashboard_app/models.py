from django.db import models

# Create your models here.

class Dashboard_Details_Model(models.Model):
    user_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.title

    class Meta:
        db_table = "user_details"

class User_Post_Model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=900)
    usr_fk= models.ForeignKey(Dashboard_Details_Model,on_delete=models.CASCADE)

    class Meta:
        db_table = "user_posts"