from django.urls import path
from . import views

urlpatterns = [
    path('', views.friend),
    path('<int:user_id>', views.profile, name="profile"),
    path('add_friend/<int:user_id>', views.add_friend, name="add_friend"),
    path('remove_friend/<int:user_id>', views.remove_friend, name="remove_friend"),
]