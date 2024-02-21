from AppTwo import views
from django.urls import path

urlpatterns=[
    path('', views.users, name='user'),
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
]

# urls.py

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # Your existing URL patterns
# ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

