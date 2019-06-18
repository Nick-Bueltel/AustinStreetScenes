from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('scenes/', views.scenes_index, name="index"),
    path('scenes/<int:scene_id>/', views.scenes_detail, name='detail'),
    path('scenes/create/', views.SceneCreate.as_view(), name='scenes_create'),
    path('scenes/<int:pk>/update', views.SceneUpdate.as_view(), name='scenes_update'),
    path('scenes/<int:pk>/delete', views.SceneDelete.as_view(), name='scenes_delete'),
    path('myposts/', views.myposts, name="myposts"),
    path('scenes/<int:scene_id>/add_photo/', views.add_photo, name='add_photo'),
]