from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.myposts.as_view(), name="myposts_list"),
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('scenes/', views.scenes_index, name="index"),
    path('scenes/<int:scene_id>/', views.scenes_detail, name='detail'),
    path('scenes/create/', views.SceneCreate.as_view(), name='scenes_create'),
    path('scenes/<int:pk>/update', views.SceneUpdate.as_view(), name='scenes_update'),
    path('scenes/<int:pk>/delete', views.SceneDelete.as_view(), name='scenes_delete'),
    path('myposts/', myposts.as_view(), name="myposts_list"),
    path('scenes/<int:scene_id>/add_photo/', views.add_photo, name='add_photo'),
]