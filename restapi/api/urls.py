from django.urls import path
from api.views import * 


urlpatterns = [
    path('user/', get_user, name='get_user'),
    path('user/create/', create_user, name='create_user'),
]