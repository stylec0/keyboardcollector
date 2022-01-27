from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for keyboards index
  path('keyboards/', views.keyboards_index, name='index'),
  path('keyboards/<int:keyboard_id>/', views.keyboards_detail, name='detail'),
  path('keyboards/<int:keyboard_id>/add_keycap', views.add_keycap, name='add_keycap'),
  path('keyboards/<int:keyboard_id>/add_stablizer/<int:stablizer_id>/', views.add_stablizer, name='add_stablizer'),
  path('keyboards/create/', views.KeyboardCreate.as_view(), name='keyboards_create'),
	path('keyboards/<int:pk>/update/', views.KeyboardUpdate.as_view(), name='keyboards_update'),
	path('keyboards/<int:pk>/delete/', views.KeyboardDelete.as_view(), name='keyboards_delete'),
  path('stablizers/', views.StablizerList.as_view(), name='stablizers_index'),
  path('stablizers/<int:pk>/', views.StablizerDetail.as_view(), name='stablizers_detail'),
  path('stablizers/create/', views.StablizerCreate.as_view(), name='stablizers_create'),
  path('stablizers/<int:pk>/update/', views.StablizerUpdate.as_view(), name='stablizers_update'),
  path('stablizers/<int:pk>/delete/', views.StablizerDelete.as_view(), name='stablizers_delete'),
]


# submit our form
# find the cat from the params id(cat_id), then add the feeding to that cat,
#
