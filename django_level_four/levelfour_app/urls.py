from django.urls import path
from levelfour_app import views


#TEMPLATE TAGGING
app_name = 'levelfour_app'


urlpatterns = [
    
    path("relative/", views.relative, name ='relative'),
    path("other/", views.other, name ='other'),
]
