from rest_framework import serializers
from user_dashboard_app.models import *


class Dashboard_Details_Serializer(serializers.ModelSerializer):
    user_name    = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    class Meta:
        model = Dashboard_Details_Model
        fields = "__all__"

class User_Post_Serializer(serializers.ModelSerializer):     
    class Meta:
        model = User_Post_Model
        fields = "__all__"