from django.urls import path
from rest_framework.authtoken import views
#from .views import api_posts, api_posts_detail

urlpatterns = [

    path('api-token-auth/', views.obtain_auth_token),

]