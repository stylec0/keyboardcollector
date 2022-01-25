from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for keyboards index
  path('keyboards/', views.keyboards_index, name='index'),
  path('keyboards/<int:keyboard_id>/', views.keyboards_detail, name='detail')
]

