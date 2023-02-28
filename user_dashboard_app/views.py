from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user_dashboard_app.models import *
from user_dashboard_app.serializer import *
# Create your views here.

def user_details(request):    
    return render(request,"index.html")

class DashboardAPI(APIView):

    def get(self,request,id=0):
        if id > 0:
            user = Dashboard_Details_Model.objects.get(id=id)
            serializer = Dashboard_Details_Serializer(user)
        else:               
            user = Dashboard_Details_Model.objects.all()
            serializer = Dashboard_Details_Serializer(user,many=True)
        return Response(serializer.data)
    
    def post(self,request):                
        serializer = Dashboard_Details_Serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()            
            return Response({"status" : "success"})
        return Response(serializer.errors)
    
    def put(self,request,id):
        user = Dashboard_Details_Model.objects.get(id=id)
        serializer = Dashboard_Details_Serializer(user,data=request.data)
        # print(serializer.data)
        if(serializer.is_valid()):
            serializer.save()            
            return Response({"status" : "success"})
        return Response(serializer.errors)

    def delete(self,request,id):        
        user = Dashboard_Details_Model.objects.get(id=id)
        user.delete()
        return Response({"status":"success"})

class User_Post_API(APIView):
    def get(self,request,id,post_id=0):        
        if post_id > 0:
            user_post = User_Post_Model.objects.filter(usr_fk=id,id=post_id)                        
            serializers = User_Post_Serializer(user_post,many=True)
        else:
            user_post = User_Post_Model.objects.filter(usr_fk=id)            
            serializers = User_Post_Serializer(user_post,many=True)
        return Response(serializers.data)

    def post(self,request,id,format=None):
        try:                                             
            serializer = User_Post_Serializer(data = request.data)            
            if(serializer.is_valid()):
                serializer.save()            
                return Response({"status" : "success"})
            return Response(serializer.errors)
        except Exception as ex:
            return Response("Error : "+str(ex))

    def put(self,request,id,post_id):
        user = User_Post_Model.objects.get(id=post_id)
        serializer = User_Post_Serializer(user,data=request.data)        
        if(serializer.is_valid()):
            serializer.save()            
            return Response({"status" : "success"})
        return Response(serializer.errors)

    def delete(self,request,id,post_id):        

        user = User_Post_Model.objects.get(id=post_id)
        user.delete()
        return Response({"status":"success"})

        