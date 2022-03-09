

from django.urls import path,include
from . import views
import blog.urls


urlpatterns = [
    path('', views.index,name='all_blogs'),
    path('/<int:id>/', views.single_blog,name='blog'),
]
