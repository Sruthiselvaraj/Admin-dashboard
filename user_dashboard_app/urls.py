from django.urls import path, include
from user_dashboard_app.views import *




urlpatterns = [            
    path('',view=user_details, name='dashboard_details'),
    path('users/',DashboardAPI.as_view(), name='dashboard_details'),
    path('users/<int:id>',DashboardAPI.as_view(), name='dashboard_details_put'),
    path('users/<int:id>/posts/',User_Post_API.as_view(), name='User_post_get'),
    path('users/<int:id>/posts/<int:post_id>',User_Post_API.as_view(), name='User_post_get_put_delete'),

]